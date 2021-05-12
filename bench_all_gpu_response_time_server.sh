HOST='148.187.39.168' # the IP of local NIC
PORT='65433'
# sleep for 60 seconds, waiting the port to be retrieved by the OS


python bench_gpu_response_server.py SIFT100M IVF1024,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 39 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF2048,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 21 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF4096,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 21 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF8192,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 22 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF16384,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 20 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF32768,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 29 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF65536,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 33 -host $HOST -port $PORT
sleep 60

python bench_gpu_response_server.py SIFT100M IVF131072,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 37 -host $HOST -port $PORT
sleep 60

#python bench_gpu_response_server.py SIFT100M IVF262144,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 49 -host $HOST -port $PORT
#sleep 60
#
#
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF1024,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 11 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF2048,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 13 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF4096,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 14 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF8192,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 17 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF16384,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 18 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF32768,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 23 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF65536,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 26 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF131072,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 33 -host $HOST -port $PORT
#sleep 60
#
#python bench_gpu_response_server.py SIFT100M OPQ16,IVF262144,PQ16 -nnn 10 -ngpu 1 -startgpu 0 -tempmem 1610612736 -qbs 1 -nprobe 45 -host $HOST -port $PORT
#sleep 60
