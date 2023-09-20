# GPU Index scan energy

## SIFT

```
python GPU_index_scanner_infininte_loop.py --dim 128 --nlist 32768 --nprobe 32 --use_gpu_id 0 --n_batch 100000 --batch_size 1
nvidia-smi -l 1 > log_energy_GPU_SIFT_1
python compute_GPU_average_energy.py --gpu_id 0 --nvidia_smi_file log_energy_GPU_SIFT_1
```

* batch size = 1: 

Average energy consumption: 183.31 W

Average time per query (ms): 0.19 ms

* batch size = 4: 

Average energy consumption: 197.43 W

Average time per query (ms): 0.048 ms

* batch size = 16: 

Average energy consumption: 213.37 W

Average time per query (ms): 0.013 ms

* batch size = 64: 

Average energy consumption: 264.84 W

Average time per query (ms): 0.004 ms



## Deep

```
python GPU_index_scanner_infininte_loop.py --dim 96 --nlist 32768 --nprobe 32 --use_gpu_id 0 --n_batch 100000 --batch_size 1
nvidia-smi -l 1 > log_energy_GPU_Deep_1
python compute_GPU_average_energy.py --gpu_id 0 --nvidia_smi_file log_energy_GPU_Deep_1
```

* batch size = 1: 

Average energy consumption: 180.07 W

Average time per query (ms): 0.190 ms

* batch size = 4: 

Average energy consumption: 192.8 W

Average time per query (ms): 0.046 ms

* batch size = 16: 

Average energy consumption: 205.07 W

Average time per query (ms): 0.012 ms

* batch size = 64: 

Average energy consumption: 243.35 W

Average time per query (ms): 0.004 ms


## RALM-S

```
python GPU_index_scanner_infininte_loop.py --dim 512 --nlist 32768 --nprobe 32 --use_gpu_id 0 --n_batch 100000 --batch_size 1
nvidia-smi -l 1 > log_energy_GPU_RALM-S_1
python compute_GPU_average_energy.py --gpu_id 0 --nvidia_smi_file log_energy_GPU_RALM-S_1
```


* batch size = 1: 

Average energy consumption: 232.33 W

Average time per query (ms): 0.258 ms

* batch size = 4: 

Average energy consumption: 288.54 W

Average time per query (ms): 0.067 ms

* batch size = 16: 

Average energy consumption: 301.17 W

Average time per query (ms): 0.018 ms

* batch size = 64: 

Average energy consumption: 346.17 W

Average time per query (ms): 0.007 ms


## RALM-L

```
python GPU_index_scanner_infininte_loop.py --dim 1024 --nlist 32768 --nprobe 32 --use_gpu_id 0 --n_batch 100000 --batch_size 1
nvidia-smi -l 1 > log_energy_GPU_RALM-L_1
python compute_GPU_average_energy.py --gpu_id 0 --nvidia_smi_file log_energy_GPU_RALM-L_1
```


* batch size = 1: 

Average energy consumption: 282.85 W

Average time per query (ms): 0.330 ms

* batch size = 4: 

Average energy consumption: 344.92 W

Average time per query (ms): 0.090 ms

* batch size = 16: 

Average energy consumption: 350.73 W

Average time per query (ms): 0.024 ms

* batch size = 64: 

Average energy consumption: 343.68 W

Average time per query (ms): 0.013 ms
