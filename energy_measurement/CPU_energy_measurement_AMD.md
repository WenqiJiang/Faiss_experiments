# CPU Energy Measurement

Use bench_polysemous_1bn.py to run a bunch of workloads, use cpu-energy-meter to measure the energy at the mean time. Iterate on nprobe=32, such that both IVF index scan and PQ code scan will be measured.

Use sgs-gpu servers (AMD EPYC 7313 16-Core Processor @ 3GHz, 7nm). Use 8 physical cores to compare with an FPGA. Here, we measure 16-core as an entire socket to get more accuracte measurement.

## Summary

Energy consumption (16 cores): 151.35 ~ 171.65 W

Energy consumption (8 cores): 75.67 ~ 85.82 W

## Idle energy

```
/usr/lib/linux-tools-5.15.0-73/turbostat --S --interval 1 > log_energy_idle_CPU_AMD
python turbostat_energy_parsing.py --fname log_energy_idle_CPU_AMD
```

2 sockets (16 x 2 = 32 cores):

Average energy consumption: 85.23 W

## SIFT

Loop over batch size = 1, 4, 16, 64

```
taskset --cpu-list 0-15 python bench_polysemous_1bn.py --on_disk 0 --dbname SIFT1000M --index_key IVF32768,PQ16 --parametersets 'nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32' --batch_size 1

/usr/lib/linux-tools-5.15.0-73/turbostat --S --interval 1 > log_energy_CPU_AMD_SIFT_1
python turbostat_energy_parsing.py --fname log_energy_CPU_AMD_SIFT_1 
```

* batch size = 1: 

Average energy consumption: 142.31 W

Average time per query (ms): 9.532 ms

Per socket (16 core): 142.31 - 131.41 / 2 = 76.60 W

Energy per query:  76.60 * 9.532 = 730.15 mJ

* batch size = 4: 

Average energy consumption: 194.72 W

Average time per query (ms): 2.853 ms

Per socket (16 core): 194.72 - 131.41 / 2 = 129.01 W

Energy per query:  129.01 * 2.853 = 368.06 mJ

* batch size = 16: 

Average energy consumption: 202.51 W

Average time per query (ms): 0.896 ms

Per socket (16 core): 202.51 - 131.41 / 2 = 136.80 W

Energy per query:  136.80 * 0.896 = 122.57 mJ

* batch size = 64: 

Average energy consumption: 206.41 W

Average time per query (ms): 0.701 ms

Per socket (16 core): 206.41 - 131.41 / 2 = 140.70 W

Energy per query:  140.70 * 0.701 = 98.63 mJ

## Deep

```
taskset --cpu-list 0-15  python bench_polysemous_1bn.py --on_disk 0 --dbname Deep1000M --index_key IVF32768,PQ16 --parametersets 'nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32' --batch_size 1

/usr/lib/linux-tools-5.15.0-73/turbostat --S --interval 1 > log_energy_CPU_AMD_Deep_1
python turbostat_energy_parsing.py --fname log_energy_CPU_AMD_Deep_1 
```

* batch size = 1: 

Average energy consumption: 140.31 W

Average time per query (ms): 9.514 ms

* batch size = 4: 

Average energy consumption: 185.01 W

Average time per query (ms): 2.900 ms


* batch size = 16: 

Average energy consumption: 219.37 W

Average time per query (ms): 0.877 ms

* batch size = 64: 

Average energy consumption: 221.81 W

Average time per query (ms): 0.707 ms


## RALM-S 


```
taskset --cpu-list 0-15 python run_RALM_SYN_dataset.py --on_disk 0 --dbname RALM-S1000M --index_key IVF32768,PQ32 --parametersets  'nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32' --batch_size 1

/usr/lib/linux-tools-5.15.0-73/turbostat --S --interval 1 > log_energy_CPU_AMD_RALM-S_1
python turbostat_energy_parsing.py --fname log_energy_CPU_AMD_RALM-S_1
```

* batch size = 1: 

Average energy consumption: 119.54 W

Average time per query (ms): 22.553 ms

* batch size = 4: 

Average energy consumption: 175.94 W

Average time per query (ms): 7.184 ms

* batch size = 16: 

Average energy consumption: 199.38 W

Average time per query (ms): 2.376 ms

* batch size = 64: 

Average energy consumption: 205.02 W

Average time per query (ms): 1.947 ms



## RALM-L 

```
taskset --cpu-list 0-15  python run_RALM_SYN_dataset.py --on_disk 0 --dbname RALM-L1000M --index_key IVF32768,PQ64 --parametersets 'nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32 nprobe=32' --batch_size 1

/usr/lib/linux-tools-5.15.0-73/turbostat --S --interval 1 > log_energy_CPU_AMD_RALM-L_1
python turbostat_energy_parsing.py --fname log_energy_CPU_AMD_RALM-L_1
```

* batch size = 1: 

Average energy consumption: 122.76 W

Average time per query (ms): 55.648 ms

* batch size = 4: 

Average energy consumption: 177.71 W

Average time per query (ms): 17.136 ms

* batch size = 16: 

Average energy consumption: 211.99 W

Average time per query (ms): 5.423 ms

* batch size = 64: 

Average energy consumption: 205.60 W

Average time per query (ms): 4.356 ms

