HOST='148.187.39.168' # the IP of local NIC
PORT='65433'

sleep 30

python bench_gpu_response_time_client.py SIFT100M IVF1024,PQ16 nprobe=39 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF2048,PQ16 nprobe=21 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF4096,PQ16 nprobe=21 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF8192,PQ16 nprobe=22 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF16384,PQ16 nprobe=20 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF32768,PQ16 nprobe=29 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF65536,PQ16 nprobe=33 $HOST $PORT
sleep 150

python bench_gpu_response_time_client.py SIFT100M IVF131072,PQ16 nprobe=37 $HOST $PORT
sleep 150

#python bench_gpu_response_time_client.py SIFT100M IVF262144,PQ16 nprobe=49 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF1024,PQ16 nprobe=11 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF2048,PQ16 nprobe=13 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF4096,PQ16 nprobe=14 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF8192,PQ16 nprobe=17 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF16384,PQ16 nprobe=18 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF32768,PQ16 nprobe=23 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF65536,PQ16 nprobe=26 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF131072,PQ16 nprobe=33 $HOST $PORT
#sleep 150
#
#python bench_gpu_response_time_client.py SIFT100M OPQ16,IVF262144,PQ16 nprobe=45 $HOST $PORT
#sleep 150


