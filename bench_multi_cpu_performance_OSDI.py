"""
This script evaluate the recall and performance of multi-shard indexes.

It first run the program on each CPU server, then gather the results to compute recall, and measure the performance.

Example: 
python bench_multi_cpu_performance_OSDI.py --dbname SBERT3000M --index_key IVF65536,PQ64 --n_shards 4 --performance_dict_dir './cpu_performance_result/m5.4xlarge_cpu_performance.pkl' --overwrite 1

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
    performance_dict_dir_shard = performance_dict_dir[:-4] + '_shard_{}'.format(shard_id)
    cmd = "python bench_cpu_performance_OSDI.py --dbname {} --index_key {} --n_shards {} --shard_id {} --performance_dict_dir {} --record_latency_distribution {} --record_computed_results {} --overwrite {}".format(
        dbname, index_key, n_shards, shard_id, performance_dict_dir_shard, record_latency_distribution, record_computed_results, overwrite)
    print("Running command:\n{}".format(cmd))
    os.system(cmd)
    performance_dict_list.append(pickle.load(performance_dict_dir_shard))

# Merge the performance results
# Make sure these numbers to be the same with bench_cpu_performance_OSDI.py
topK = 100
qbs_list = [1, 2, 4, 8, 16, 32, 64]
qbs_list.reverse() # using large batches first since they are faster
nprobe_list = [1, 2, 4, 8, 16, 32, 64, 128]

"""
Input dict format

The results are saved as an dictionary which has the following format:
    dict[dbname][index_key][qbs][nprobe] contains several components:
    dict[dbname][index_key][qbs][nprobe]["R1@1"]
    dict[dbname][index_key][qbs][nprobe]["R1@10"]
    dict[dbname][index_key][qbs][nprobe]["R1@100"]
    dict[dbname][index_key][qbs][nprobe]["R@1"]
    dict[dbname][index_key][qbs][nprobe]["R@10"]
    dict[dbname][index_key][qbs][nprobe]["R@100"]
    dict[dbname][index_key][qbs][nprobe]["QPS"]
    dict[dbname][index_key][qbs][nprobe]["latency@50"] in ms
    dict[dbname][index_key][qbs][nprobe]["latency@95"] in ms

    optional (record_latency_distribution == 1): 
    dict[dbname][index_key][qbs][nprobe]["latency_distribution"] -> a list of latency (of batches) in ms

    optional (record_computed_results == 1):
    dict[dbname][index_key][ngpu][qbs][nprobe]["I"] -> idx, shape = np.empty((nq, topK), dtype='int64')
    dict[dbname][index_key][ngpu][qbs][nprobe]["D"] -> dist, shape = np.empty((nq, topK), dtype='float32')
"""

# for qbs in qbs_list:

#     print("batch size: ", qbs)
#     sys.stdout.flush()
#     if qbs not in dict_perf[dbname][index_key]:
#         dict_perf[dbname][index_key][qbs] = dict()

#     for nprobe in nprobe_list:
