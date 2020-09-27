from os import listdir
from os.path import isfile, join
import pickle
    
mypath="./cpu_performance_result/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] 
onlyfiles = [f for f in onlyfiles if f[0] != '.'] # remove hidden files
print(onlyfiles)

def save_obj(obj, dire, name):
    with open(dire + name + '.pkl', 'wb') as fl:
        pickle.dump(obj, fl, pickle.HIGHEST_PROTOCOL)

for file_name in onlyfiles:
    with open(mypath + file_name, 'r') as f:
        print(file_name)
        lines = f.readlines() 

        print('\n' + file_name)
        all_elements = []
        # Strips the newline character 
        for line in lines: 
            line = line.replace("\xa0", "").replace("\n", "").split(" ")
            # print(line)
            elements = [e for e in line if e != ""]
            # print(elements)
            assert len(elements) == 6
            all_elements.append(elements)

        print("dictionary keys: nprobe, R1, R10, R100, time")
        nprobe = [int(e[0][7:]) for e in all_elements] # "nprobe=1024, remove the prefix"
        R1 = [float(e[1]) for e in all_elements]
        R10 = [float(e[2]) for e in all_elements]
        R100 = [float(e[3]) for e in all_elements]
        time = [float(e[4]) for e in all_elements]
        # the last column is the pass rate of polynomeous code, not needed
        total_cells = 0
        if "IMI2x" in file_name:
            total_cells = (2 ** int(file_name[5:7])) ** 2
        else:
            seg = file_name.split(",")
            for s in seg:
                if "IVF" in s:
                    total_cells = int(s[3:])
        scanned_ratio = [np / total_cells for np in nprobe]

        # the final dictionary that contain all info of this set of experiments
        info = dict()
        info["nprobe"] = nprobe
        info["total_cells"] = total_cells
        info["scanned_ratio"] = scanned_ratio
        info["R1"] = R1
        info["R10"] = R10
        info["R100"] = R100
        info["time"] = time
        print(info)
        save_obj(info, "./cpu_performance_result/dict/", file_name)