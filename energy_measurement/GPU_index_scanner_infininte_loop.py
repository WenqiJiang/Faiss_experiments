import faiss
import numpy as np
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--dim', type=int, default=128)
parser.add_argument('--nlist', type=int, default=32768)
parser.add_argument('--nprobe', type=int, default=32)
parser.add_argument('--use_gpu_id', type=int, default=0)
parser.add_argument('--n_batch', type=int, default=10000)
parser.add_argument('--batch_size', type=int, default=1)

args = parser.parse_args()
dim = args.dim
nlist = args.nlist
nprobe = args.nprobe
use_gpu_id = args.use_gpu_id
n_batch = args.n_batch
batch_size = args.batch_size

index = faiss.IndexFlatL2(dim)
centroids = np.random.rand(nlist, dim).astype('float32')
index.add(centroids)

resource = faiss.StandardGpuResources()
index = faiss.index_cpu_to_gpu(resource, use_gpu_id, index) # 1 as ID

random_query = np.random.rand(n_batch * batch_size, dim).astype('float32')
total_time = 0
for i in range(n_batch):
	print("Batch {}".format(i))
	start = time.time()
	index.search(random_query[i * batch_size : (i + 1) * batch_size], nprobe)
	end = time.time()
	total_time += end - start
	print("This batch: Per query time: {:.3f} ms".format((end - start) * 1000 / batch_size))
	print("Overall: Per query time: {:.3f} ms".format(total_time * 1000 / ((i + 1) * batch_size)))
