# Faiss_experiments

## Installation

install anaconda: https://docs.anaconda.com/anaconda/install/linux/

% faiss supports python3.7, not 3.8

conda create -n py37 python=3.7

conda activate py37

% install openblas

conda install -c conda-forge openblas

% either install cpu or gpu version (the gpu version already includes the cpu version, thus can skip the cpu installation step)

% cpu version 

conda install -c pytorch faiss-cpu

% install gpu version (version 1.6.3)

conda install faiss-gpu cudatoolkit=10.0 -c pytorch

% verify installation

python 

import faiss

% Faiss's demo: 
https://github.com/facebookresearch/faiss/blob/master/tutorial/python/1-Flat.py

% Faiss API: 
https://github.com/facebookresearch/faiss/wiki/Faiss-indexes

## Directory Navigation

### bench_polysemous_1bn.py

Train / query a single index on CPU.

### train_cpu.py

Train a combination of indexes (IMI / IVF Cell number; PQ code length; with OPQ or not; dataset) on CPU.

To cover all indexes on SIFT100M dataset: 

```
python train_cpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 1

python train_cpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 0

python train_cpu.py --dataset SIFT100M --index IMI --PQ 16

python train_cpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 1

python train_cpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 0

python train_cpu.py --dataset SIFT100M --index IMI --PQ 8
```

### performance_test_cpu.py

Test the performance for trained indexes, and output the recall / performance in "./cpu_performance_result"

To cover all indexes on SIFT100M dataset:  

```
python performance_test_cpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 1

python performance_test_cpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 0

python performance_test_cpu.py --dataset SIFT100M --index IMI --PQ 16

python performance_test_cpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 1

python performance_test_cpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 0

python performance_test_cpu.py --dataset SIFT100M --index IMI --PQ 8
```

### bench_gpu_1bn.py

Train / query a single index on GPU.

```
python bench_gpu_1bn.py SIFT1000M OPQ16,IVF262144,PQ16 -nnn 100 -ngpu 3 -startgpu 1 -tempmem $[1536*1024*1024] -qbs 512
```

### train_gpu.py

Automatically train a set of indexes on GPU.

To cover all indexes on SIFT100M dataset:  

```
python train_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 1 --ngpu 4 --startgpu 3

python train_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 0 --ngpu 4 --startgpu 3

python train_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 1 --ngpu 4 --startgpu 3

python train_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 0 --ngpu 4 --startgpu 3
```

### performance_test_gpu.py

Test the performance for trained indexes, and output the recall / performance in "./cpu_performance_result"

To cover all indexes on SIFT100M dataset:  

```
python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 1 --ngpu 1 --startgpu 5

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 0 --ngpu 1 --startgpu 5

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 1 --ngpu 1 --startgpu 5

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 0 --ngpu 1 --startgpu 5
```

### save_performance_log_as_dict.py

Given the output log (recall / time result) printed by Faiss CPU / GPU, save these numbers in the form of python dictionary, and print the contents out.

## GPU Experiments

## CPU Experiments

### IVF

python bench_polysemous_1bn.py SIFT100M IVF8192,PQ16 nprobe=1 nprobe=2 nprobe=4 nprobe=8 nprobe=16 nprobe=32 nprobe=64 nprobe=128

### IMI

python bench_polysemous_1bn.py SIFT100M IMI2x14,PQ16 nprobe=1 nprobe=2 nprobe=4 nprobe=8 nprobe=16 nprobe=32 nprobe=64 nprobe=128 nprobe=256 nprobe=512 nprobe=1024 nprobe=2048 nprobe=4096 nprobe=8192 nprobe=16384 nprobe=32768 nprobe=65536 
