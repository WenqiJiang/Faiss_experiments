
import argparse 
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--fname', type=str, default='log_energy_idle')

args = parser.parse_args()
fname = args.fname

energy_array = []
with open(fname) as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		if i >= 1:
			energy = float(line.split()[-1])
			energy_array.append(energy)
print("Average energy consumption: {:.2f} W".format(np.average(energy_array)))
