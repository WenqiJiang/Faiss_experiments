#!/usr/bin/env python3

import socket
import numpy as np
import time
import sys

"""
Send 10000 queries to the server

e.g., 
python bench_cpu_response_time_client.py SIFT100M OPQ16,IVF4096,PQ16 nprobe=32 127.0.0.1 65432
"""

# python socket tutorial: https://realpython.com/python-sockets/#socket-api-overview

#### Change server's host IP when needed ####

dbname        = sys.argv[1]
index_key     = sys.argv[2]
param         = sys.argv[3]
HOST          = sys.argv[4] # e.g., '127.0.0.1', set to physical interface if needed
PORT          = int(sys.argv[5]) # e.g., 65432

BYTES_PER_RESULT = 10 * 4 # top 10, int32

def mmap_fvecs(fname):
    x = np.memmap(fname, dtype='int32', mode='r')
    d = x[0]
    return x.view('float32').reshape(-1, d + 1)[:, 1:]


def mmap_bvecs(fname):
    x = np.memmap(fname, dtype='uint8', mode='r')
    d = x[:4].view('int32')[0]
    return x.reshape(-1, d + 4)[:, 4:]


xq = mmap_bvecs('bigann/bigann_query.bvecs')
xq = xq.astype('float32').copy()
xq = np.array(xq, dtype=np.float32)

nq, d = xq.shape

query_vecs = []
for i in range(nq):
    query_vec = xq[i]
    query_vec = np.reshape(query_vec, (1,128))
    query_vec = query_vec.tostring()
    query_vecs.append(query_vec)

response_time = [] # in terms of ms

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for i in range(nq):
        t0 = time.time()
        s.sendall(query_vecs[i])
        I = s.recv(BYTES_PER_RESULT) # top 10 * 4 bytes
        I = np.fromstring(I, dtype=np.int32)
        t1 = time.time()
        response_time.append(1000 * (t1 - t0)) 

    response_time = np.array(response_time, dtype=np.float32)
    
    np.save('./CPU_response_time/CPU_response_time_{}_{}_{}'.format(dbname, index_key, param), 
        response_time)
