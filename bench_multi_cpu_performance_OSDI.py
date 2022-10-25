"""
This script evaluate the recall and performance of multi-shard indexes.

It first run the program on each CPU server, then gather the results to compute recall, and measure the performance.
"""

from __future__ import print_function
import os
import sys
import time
import numpy as np
import re
import pickle
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--dbname', type=str, default='SIFT100M', help="dataset name, e.g., SIFT100M")
parser.add_argument('--index_key', type=str, default='IVF4096,PQ16', help="index parameters, e.g., IVF4096,PQ16 or OPQ16,IVF4096,PQ16")
parser.add_argument('--n_shards', type=int, default=None, help="e.g., can use 2 or 4 shards for large datasets")
parser.add_argument('--overwrite', type=int, default=0, help="whether to overwrite existed performance, by default, skip existed settings")
parser.add_argument('--performance_dict_dir', type=str, default='./cpu_performance_result/cpu_throughput_SIFT100M.pkl', help="a dictionary of d[dbname][index_key][topK][recall_goal] -> throughput (QPS)")

args = parser.parse_args()

dbname = args.dbname
index_key = args.index_key
n_shards = args.n_shards
overwrite = args.overwrite
performance_dict_dir = args.performance_dict_dir

record_latency_distribution = 1 # always record latency distribution
record_computed_results = 1 # always record results
assert performance_dict_dir[-4:] == '.pkl'


# evaluate the performance results
performance_dict_list = []
for shard_id in range(n_shards):
    performance_dict_dir_shard = performance_dict_dir[:-4] + 'shard_{}'.format(shard_id)
    cmd = "python bench_cpu_performance_OSDI.py --dbname {} --index_key {} --n_shards {} --shard_id {} --performance_dict_dir {} --record_latency_distribution {} --record_computed_results{} --overwrite {}".format(
        dbname, index_key, n_shards, shard_id, performance_dict_dir_shard, record_latency_distribution, record_computed_results, overwrite)
    print("Running command:\n{}".format(cmd))
    os.sys(cmd)
    performance_dict_list.append(pickle.load(performance_dict_dir_shard))

# Merge the performance results
# Make sure these numbers to be the same with bench_cpu_performance_OSDI.py
topK = 100
qbs_list = [1, 2, 4, 8, 16, 32, 64]
qbs_list.reverse() # using large batches first since they are faster
nprobe_list = [1, 2, 4, 8, 16, 32, 64, 128]
