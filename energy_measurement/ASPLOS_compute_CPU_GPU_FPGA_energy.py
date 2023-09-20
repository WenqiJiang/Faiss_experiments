import numpy as np


def get_CPU_energy():

	idle_power_two_sockets = 85.23 

	CPU_power_two_sockets = {}

	CPU_power_two_sockets['SIFT'] = {}
	CPU_power_two_sockets['SIFT'][1] = 142.31
	CPU_power_two_sockets['SIFT'][4] = 194.72
	CPU_power_two_sockets['SIFT'][16] = 202.51
	CPU_power_two_sockets['SIFT'][64] = 206.41

	CPU_power_two_sockets['Deep'] = {}
	CPU_power_two_sockets['Deep'][1] = 140.31
	CPU_power_two_sockets['Deep'][4] = 185.01
	CPU_power_two_sockets['Deep'][16] = 204.37
	CPU_power_two_sockets['Deep'][64] = 205.81

	CPU_power_two_sockets['RALM-S'] = {}
	CPU_power_two_sockets['RALM-S'][1] = 119.54
	CPU_power_two_sockets['RALM-S'][4] = 175.94
	CPU_power_two_sockets['RALM-S'][16] = 199.38
	CPU_power_two_sockets['RALM-S'][64] = 205.02

	CPU_power_two_sockets['RALM-L'] = {}
	CPU_power_two_sockets['RALM-L'][1] = 122.76
	CPU_power_two_sockets['RALM-L'][4] = 177.71
	CPU_power_two_sockets['RALM-L'][16] = 211.99
	CPU_power_two_sockets['RALM-L'][64] = 205.60 

	# 16 cores
	CPU_power_one_socket = {}
	for dbname in CPU_power_two_sockets:
		CPU_power_one_socket[dbname] = {}
		for n in CPU_power_two_sockets[dbname]:
			CPU_power_one_socket[dbname][n] = CPU_power_two_sockets[dbname][n] - idle_power_two_sockets / 2

	CPU_time_per_query_ms = {}
	CPU_time_per_query_ms['SIFT'] = {}
	CPU_time_per_query_ms['SIFT'][1] = 9.532 
	CPU_time_per_query_ms['SIFT'][4] = 2.853
	CPU_time_per_query_ms['SIFT'][16] = 0.896
	CPU_time_per_query_ms['SIFT'][64] = 0.701

	CPU_time_per_query_ms['Deep'] = {}
	CPU_time_per_query_ms['Deep'][1] = 9.514
	CPU_time_per_query_ms['Deep'][4] = 2.900
	CPU_time_per_query_ms['Deep'][16] = 0.877
	CPU_time_per_query_ms['Deep'][64] = 0.700

	CPU_time_per_query_ms['RALM-S'] = {}
	CPU_time_per_query_ms['RALM-S'][1] = 22.553
	CPU_time_per_query_ms['RALM-S'][4] = 7.184
	CPU_time_per_query_ms['RALM-S'][16] = 2.376
	CPU_time_per_query_ms['RALM-S'][64] = 1.947 

	CPU_time_per_query_ms['RALM-L'] = {}
	CPU_time_per_query_ms['RALM-L'][1] = 55.648
	CPU_time_per_query_ms['RALM-L'][4] = 17.136
	CPU_time_per_query_ms['RALM-L'][16] = 5.423
	CPU_time_per_query_ms['RALM-L'][64] = 4.356

	CPU_energy_per_query_mJ = {} 
	for dbname in CPU_time_per_query_ms:
		CPU_energy_per_query_mJ[dbname] = {}
		for n in CPU_time_per_query_ms[dbname]:
			CPU_energy_per_query_mJ[dbname][n] = CPU_power_one_socket[dbname][n] * CPU_time_per_query_ms[dbname][n] 
	
	return CPU_energy_per_query_mJ

def get_FPGA_energy():
	""" FPGA for PQ code scan, energy from Vivado """
	per_FPGA_bandwidth = 32 * 1e9 # 32 GB/s
	FPGA_energy_per_query_mJ = {}

	for dbname in ['SIFT', 'Deep', 'RALM-S', 'RALM-L']:
		if dbname == 'SIFT':
			dim = 128
			m = 16
			FPGA_power = 38.4
		elif dbname == 'Deep':
			dim = 96
			m = 16
			FPGA_power = 37.0
		elif dbname == 'RALM-S':
			dim = 512
			m = 32
			FPGA_power = 36.5
		elif dbname == 'RALM-L':
			dim = 1024
			m = 64
			FPGA_power = 39.3
		scanned_bytes = 32 / 32768 * m * 1e9
		query_time_ms = scanned_bytes / per_FPGA_bandwidth * 1000
		per_query_mJ = FPGA_power * query_time_ms

		FPGA_energy_per_query_mJ[dbname] = {}
		for n in [1, 4, 16, 64]:
			FPGA_energy_per_query_mJ[dbname][n] = per_query_mJ

	return FPGA_energy_per_query_mJ

def get_GPU_energy():
	"""
	GPU index scan energy
	"""

	GPU_power = {}
	GPU_time_per_query_ms = {}

	GPU_power['SIFT'] = {}
	GPU_power['SIFT'][1] = 183.31
	GPU_power['SIFT'][4] = 197.43
	GPU_power['SIFT'][16] = 213.37
	GPU_power['SIFT'][64] = 264.84

	GPU_time_per_query_ms['SIFT'] = {}
	GPU_time_per_query_ms['SIFT'][1] = 0.19
	GPU_time_per_query_ms['SIFT'][4] = 0.048
	GPU_time_per_query_ms['SIFT'][16] = 0.013
	GPU_time_per_query_ms['SIFT'][64] = 0.004 

	GPU_power['Deep'] = {}
	GPU_power['Deep'][1] = 180.07
	GPU_power['Deep'][4] = 192.8
	GPU_power['Deep'][16] = 205.07
	GPU_power['Deep'][64] = 243.35

	GPU_time_per_query_ms['Deep'] = {}
	GPU_time_per_query_ms['Deep'][1] = 0.190
	GPU_time_per_query_ms['Deep'][4] = 0.046
	GPU_time_per_query_ms['Deep'][16] = 0.012
	GPU_time_per_query_ms['Deep'][64] = 0.004 

	GPU_power['RALM-S'] = {}
	GPU_power['RALM-S'][1] = 232.33
	GPU_power['RALM-S'][4] = 288.54
	GPU_power['RALM-S'][16] = 301.17
	GPU_power['RALM-S'][64] = 346.17

	GPU_time_per_query_ms['RALM-S'] = {}
	GPU_time_per_query_ms['RALM-S'][1] = 0.258
	GPU_time_per_query_ms['RALM-S'][4] = 0.067
	GPU_time_per_query_ms['RALM-S'][16] = 0.018
	GPU_time_per_query_ms['RALM-S'][64] = 0.007

	GPU_power['RALM-L'] = {}
	GPU_power['RALM-L'][1] = 282.85
	GPU_power['RALM-L'][4] = 344.92
	GPU_power['RALM-L'][16] = 350.73
	GPU_power['RALM-L'][64] = 343.68

	GPU_time_per_query_ms['RALM-L'] = {}
	GPU_time_per_query_ms['RALM-L'][1] = 0.330
	GPU_time_per_query_ms['RALM-L'][4] = 0.090
	GPU_time_per_query_ms['RALM-L'][16] = 0.024
	GPU_time_per_query_ms['RALM-L'][64] = 0.013

	# compute energy 
	GPU_energy_per_query_mJ = {}
	for dbname in GPU_power:
		GPU_energy_per_query_mJ[dbname] = {}
		for n in GPU_power[dbname]:
			GPU_energy_per_query_mJ[dbname][n] = GPU_power[dbname][n] * GPU_time_per_query_ms[dbname][n]

	return GPU_energy_per_query_mJ

if __name__ == "__main__":

	CPU_energy_per_query_mJ = get_CPU_energy()
	print(CPU_energy_per_query_mJ)

	FPGA_energy_per_query_mJ = get_FPGA_energy()
	print(FPGA_energy_per_query_mJ)

	GPU_energy_per_query_mJ = get_GPU_energy()
	print(GPU_energy_per_query_mJ)

	GPU_FPGA_energy_per_query_mJ = {}
	for dbname in CPU_energy_per_query_mJ:
		GPU_FPGA_energy_per_query_mJ[dbname] = {}
		for n in CPU_energy_per_query_mJ[dbname]:
			GPU_FPGA_energy_per_query_mJ[dbname][n] = GPU_energy_per_query_mJ[dbname][n] + FPGA_energy_per_query_mJ[dbname][n]

	# Compare CPU with GPU + FPGA
	for dbname in CPU_energy_per_query_mJ:
		print("DB: {}".format(dbname))
		for n in CPU_energy_per_query_mJ[dbname]:
			print("batch size: {}\tCPU: {:.2f} mJ\tGPU+FPGA: {:.2f} mJ\t (GPU: {:.2f} mJ, FPGA: {:.2f} mJ), Efficiency: {:.2f}x".format(n, 
				CPU_energy_per_query_mJ[dbname][n], GPU_FPGA_energy_per_query_mJ[dbname][n],
				GPU_energy_per_query_mJ[dbname][n], FPGA_energy_per_query_mJ[dbname][n],
				CPU_energy_per_query_mJ[dbname][n] / GPU_FPGA_energy_per_query_mJ[dbname][n]))
