HOST='10.1.212.74' # the IP of local NIC
PORT='65432'
# sleep for 60 seconds, waiting the port to be retrieved by the OS

# python bench_cpu_response_time_server.py SIFT100M IVF2048,PQ16 nprobe=28 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF4096,PQ16 nprobe=29 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF8192,PQ16 nprobe=22 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF16384,PQ16 nprobe=29 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF32768,PQ16 nprobe=29 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF65536,PQ16 nprobe=33 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF131072,PQ16 nprobe=40 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IVF262144,PQ16 nprobe=45 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF1024,PQ16 nprobe=13 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF2048,PQ16 nprobe=13 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF4096,PQ16 nprobe=17 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF8192,PQ16 nprobe=17 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF16384,PQ16 nprobe=21 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF32768,PQ16 nprobe=24 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF65536,PQ16 nprobe=30 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF131072,PQ16 nprobe=37 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M OPQ16,IVF262144,PQ16 nprobe=42 $HOST $PORT >> cpu_response
# sleep 60


# python bench_cpu_response_time_server.py SIFT100M IMI2x8,PQ16 nprobe=96 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x9,PQ16 nprobe=114 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x10,PQ16 nprobe=151 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x11,PQ16 nprobe=258 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x12,PQ16 nprobe=356 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x13,PQ16 nprobe=677 $HOST $PORT >> cpu_response
# sleep 60

# python bench_cpu_response_time_server.py SIFT100M IMI2x14,PQ16 nprobe=1262 $HOST $PORT >> cpu_response
# sleep 60



python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x8,PQ16 nprobe=219 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x9,PQ16 nprobe=210 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x10,PQ16 nprobe=308 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x11,PQ16 nprobe=340 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x12,PQ16 nprobe=710 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x13,PQ16 nprobe=1019 $HOST $PORT >> cpu_response
sleep 60

python bench_cpu_response_time_server.py SIFT100M OPQ16,IMI2x14,PQ16 nprobe=1809 $HOST $PORT >> cpu_response
sleep 60
