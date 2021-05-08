# How to bench CPU performance?

## Throughput

For throughput test, we consider the best case that all query vectors are stored locally.

We consider the nprobe that allow the recall just to hit 80%.

To perform the tests:

```
python bench_cpu_throughput.py SIFT100M IVF2048,PQ16 nprobe=28 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF4096,PQ16 nprobe=29 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF8192,PQ16 nprobe=22 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF16384,PQ16 nprobe=29 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF32768,PQ16 nprobe=29 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF65536,PQ16 nprobe=33 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF131072,PQ16 nprobe=40 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IVF262144,PQ16 nprobe=45 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF1024,PQ16 nprobe=13 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF2048,PQ16 nprobe=13 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF4096,PQ16 nprobe=17 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF8192,PQ16 nprobe=17 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF16384,PQ16 nprobe=21 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF32768,PQ16 nprobe=24 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF65536,PQ16 nprobe=30 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF131072,PQ16 nprobe=37 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M OPQ16,IVF262144,PQ16 nprobe=42 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x8,PQ16 nprobe=96 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x9,PQ16 nprobe=114 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x10,PQ16 nprobe=151 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x11,PQ16 nprobe=258 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x12,PQ16 nprobe=356 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x13,PQ16 nprobe=677 >> cpu_throughput

python bench_cpu_throughput.py SIFT100M IMI2x14,PQ16 nprobe=1262 >> cpu_throughput
```

## Response time

We consider a client sending query to an ANNS server, and measure the response time on the client side.

To conduct the experiments, first adjust IP and port used on the server in two scripts, i.e., bench_all_cpu_response_time_server.sh and bench_all_cpu_response_time_client.sh

Then execute the scripts, on the server side:

```
./bench_all_cpu_response_time_server.sh
```

On client:

```
./bench_all_cpu_response_time_client.sh
```

The response time of every single query will be saved in folder CPU_response_time.

The measured time includes both network RTT and ANNS searching time. To measure the network RTT alone, on server side:

```
python network_RTT_server.py
```

on the client side:

```
python network_RTT_client.py
```

The client will save a networt RTT distribution named network_response_time.npy

## Unused scripts

In folder archieved_scripts, don't use them.

performance_test_cpu.py

performance_test_gpu.py