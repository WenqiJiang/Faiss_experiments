"""
This script is used to compute the ground truth for datasets, e.g., Deep100M

Usage:
    python compute_ground_truth.py --dbname Deep1M
"""

from __future__ import print_function
import os
import sys
import time
import numpy as np
import re
import argparse 
import gc
import faiss
from datasets import read_deep_fbin, read_deep_ibin, write_deep_fbin, write_deep_ibin

from multiprocessing.dummy import Pool as ThreadPool

parser = argparse.ArgumentParser()
parser.add_argument('--dbname', type=str, default='Deep1M', help='Deep1M, Deep1000M, Deep10000M')

args = parser.parse_args()

dbname = args.dbname



if dbname.startswith('Deep'):
    # Deep1M to Deep1000M
    dataset_dir = './deep1b'
    assert dbname[:4] == 'Deep' 
    assert dbname[-1] == 'M'
    dbsize = int(dbname[4:-1]) # in million
    xb = read_deep_fbin('deep1b/base.1B.fbin')[:dbsize * 1000 * 1000]
    xq = read_deep_fbin('deep1b/query.public.10K.fbin')

    # Wenqi: load xq to main memory and reshape
    xq = xq.astype('float32').copy()
    xq = np.array(xq, dtype=np.float32)

    nb, D = xb.shape # same as SIFT
    query_num = xq.shape[0]
    print('query shape: ', xq.shape)

else:
    print('unknown dataset', dbname, file=sys.stderr)
    sys.exit(1)


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

gt_topK = 1000

""" compute ground truth """
gt_dist_dir = os.path.join(dataset_dir, "gt_dis_{}M.fbin".format(dbsize))
gt_id_dir = os.path.join(dataset_dir, "gt_idx_{}M.ibin".format(dbsize))

if os.path.exists(gt_dist_dir) or os.path.exists(gt_id_dir):
    print("Ground truth data already exist, skip...")
else:
    print("Computing ground truth...")

    """ add data to index """
    print("Adding data to Flat index...")
    index = faiss.index_factory(D, "IVF1,Flat")
    index.train(np.zeros(D, dtype='float32').reshape(1,D))
    # index = faiss.IndexFlatL2(D) # IndexFlat does not support add_with_ids

    i0 = 0
    t0 = time.time()
    add_batch_size = 100000
    for xs in matrix_slice_iterator(xb, add_batch_size):
        i1 = i0 + xs.shape[0]
        print('\radd %d:%d, %.3f s' % (i0, i1, time.time() - t0), end=' ')
        sys.stdout.flush()
        index.add_with_ids(xs, np.arange(i0, i1))
        i0 = i1
    
    """ search """
    print("Searching")
    gt_dist, gt_id = index.search(xq, gt_topK)

    gt_dist = np.array(gt_dist, dtype='float32')
    gt_id = np.array(gt_id, dtype='int32')
    print("dist shape: ", gt_dist.shape)
    print("ID shape", gt_id.shape)
    write_deep_fbin(gt_dist_dir, gt_dist)
    write_deep_ibin(gt_id_dir, gt_id)

