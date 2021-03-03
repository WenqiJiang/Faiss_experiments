# Faiss_experiments

## Installation

install anaconda: https://docs.anaconda.com/anaconda/install/linux/

# init conda ，加到~/.bashrc里
source /home/wenqi/anaconda3/bin/activate

# faiss只支持到3.7
conda create -n py37 python=3.7
conda activate py37

# install openblas，复制进Commandline可能会出错，手动敲比较好
conda install -c conda-forge openblas

# 出问题的一步，很多comment说conda完全不可靠 -> 不支持py3.8
conda install -c pytorch faiss-cpu

# 看看是否安装成功
python 
import faiss

可以运行git faiss的tutorial demo: 
https://github.com/facebookresearch/faiss/blob/master/tutorial/python/1-Flat.py

Faiss API: 
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

### print_cpu_performance.py

Given the output recall / time result by Faiss, save these numbers in the form of python dictionary, and print the contents out.

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
python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 1 --ngpu 1 --startgpu 0

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 16 --OPQ 0 --ngpu 1 --startgpu 0

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 1 --ngpu 1 --startgpu 0

python performance_test_gpu.py --dataset SIFT100M --index IVF --PQ 8 --OPQ 0 --ngpu 1 --startgpu 0
```

## GPU Experiments

## CPU Experiments

### IVF

python bench_polysemous_1bn.py SIFT100M IVF8192,PQ16 nprobe=1 nprobe=2 nprobe=4 nprobe=8 nprobe=16 nprobe=32 nprobe=64 nprobe=128

### IMI

python bench_polysemous_1bn.py SIFT100M IMI2x14,PQ16 nprobe=1 nprobe=2 nprobe=4 nprobe=8 nprobe=16 nprobe=32 nprobe=64 nprobe=128 nprobe=256 nprobe=512 nprobe=1024 nprobe=2048 nprobe=4096 nprobe=8192 nprobe=16384 nprobe=32768 nprobe=65536 
