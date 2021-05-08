#!/usr/bin/env python3

from __future__ import print_function
import os
import sys
import time
import numpy as np
import re
import faiss
from multiprocessing.dummy import Pool as ThreadPool
from datasets import ivecs_read

import socket

"""
Receive 10000 queries, and perform search

e.g., 
python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF4096,PQ16 nprobe=32 127.0.0.1 65432
"""

# python socket tutorial: https://realpython.com/python-sockets/#socket-api-overview


# python socket tutorial: https://realpython.com/python-sockets/#socket-api-overview
BYTES_PER_QUERY = 128 * 4
QUERY_NUM = 10000

dbname        = sys.argv[1]
index_key     = sys.argv[2]
param         = sys.argv[3]
HOST          = sys.argv[4] # e.g., '127.0.0.1', set to physical interface if needed
PORT          = int(sys.argv[5]) # e.g., 65432 Port to listen on


def mmap_fvecs(fname):
    x = np.memmap(fname, dtype='int32', mode='r')
    d = x[0]
    return x.view('float32').reshape(-1, d + 1)[:, 1:]


def mmap_bvecs(fname):
    x = np.memmap(fname, dtype='uint8', mode='r')
    d = x[:4].view('int32')[0]
    return x.reshape(-1, d + 4)[:, 4:]


#################################################################
# Bookkeeping
#################################################################

tmpdir = './trained_CPU_indexes/bench_cpu_{}_{}'.format(dbname, index_key)

if not os.path.isdir(tmpdir):
    print("%s does not exist, creating it" % tmpdir)
    os.mkdir(tmpdir)


#################################################################
# Prepare dataset
#################################################################


print("Preparing dataset", dbname)

if dbname.startswith('SIFT'):
    # SIFT1M to SIFT1000M
    dbsize = int(dbname[4:-1])
    xq = mmap_bvecs('bigann/bigann_query.bvecs')

    gt = ivecs_read('bigann/gnd/idx_%dM.ivecs' % dbsize)

    # Wenqi: load xq to main memory and reshape
    xq = xq.astype('float32').copy()
    xq = np.array(xq, dtype=np.float32)
    gt = np.array(gt, dtype=np.int32)

else:
    print('unknown dataset', dbname, file=sys.stderr)
    sys.exit(1)

nq, d = xq.shape
assert gt.shape[0] == nq


#################################################################
# Training
#################################################################


def choose_train_size(index_key):

    # some training vectors for PQ and the PCA
    n_train = 256 * 1000

    if "IVF" in index_key:
        matches = re.findall('IVF([0-9]+)', index_key)
        ncentroids = int(matches[0])
        n_train = max(n_train, 100 * ncentroids)
    elif "IMI" in index_key:
        matches = re.findall('IMI2x([0-9]+)', index_key)
        nbit = int(matches[0])
        n_train = max(n_train, 256 * (1 << nbit))
    return n_train


def get_trained_index():
    filename = "%s/%s_%s_trained.index" % (
        tmpdir, dbname, index_key)

    if os.path.exists(filename):
        print("loading", filename)
        index = faiss.read_index(filename)
    else:
        raise ValueError("no index file")
    return index


#################################################################
# Adding vectors to dataset
#################################################################

def rate_limited_imap(f, l):
    'a thread pre-processes the next element'
    pool = ThreadPool(1)
    res = None
    for i in l:
        res_next = pool.apply_async(f, (i, ))
        if res:
            yield res.get()
        res = res_next
    yield res.get()

def matrix_slice_iterator(x, bs):
    " iterate over the lines of x in blocks of size bs"
    nb = x.shape[0]
    block_ranges = [(i0, min(nb, i0 + bs))
                    for i0 in range(0, nb, bs)]

    return rate_limited_imap(
        lambda i01: x[i01[0]:i01[1]].astype('float32').copy(),
        block_ranges)


def get_populated_index():

    filename = "%s/%s_%s_populated.index" % (
        tmpdir, dbname, index_key)

    if not os.path.exists(filename):
        raise ValueError("index file not found")
    else:
        print("loading", filename)
        index = faiss.read_index(filename)
    return index


#################################################################
# Perform searches
#################################################################

index = get_populated_index()

ps = faiss.ParameterSpace()
ps.initialize(index)

# a static C++ object that collects statistics about searches
ivfpq_stats = faiss.cvar.indexIVFPQ_stats
ivf_stats = faiss.cvar.indexIVF_stats

# we do queries in a single thread
faiss.omp_set_num_threads(1)

# Load the database by performing 1 single search
sample_vec = np.zeros((1,128), dtype=np.float32)

print(param, '\t', end=' ')
sys.stdout.flush()
ps.set_index_parameters(index, param)
ivfpq_stats.reset()
ivf_stats.reset()

D, I = index.search(sample_vec, 10)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("start listening")
    s.listen()
    conn, addr = s.accept()
    t0 = time.time()

    with conn:
        print('Connected by', addr)
        for i in range(QUERY_NUM):
            s = conn.recv(BYTES_PER_QUERY)
            query_vec = np.fromstring(s, dtype=np.float32)
            query_vec = np.reshape(query_vec, (1, 128))
            D, I = index.search(query_vec, 10)
            I = np.array(I, dtype=np.int32)
            I = I.tostring()
            conn.sendall(I)

    t1 = time.time()
    print("QPS = {} (using a single client)".format(QUERY_NUM / (t1 - t0)))