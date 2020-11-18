# Filter PPI with the interested genes only
# Lourdes B. Cajica
# 10 - 25 - 20

import os
import time

path = "C:/Users/hp/Desktop/redes_data/output/"
output_ppi = list()
temp = list()

print("reading files...", end = "")

file_ppi = open(path + "output_ppi.txt", "r")
data_ppi = file_ppi.readlines()
file_ppi.close()

print("finished. \nfiltering genes...")

id = 0
for p in data_ppi:
    prep = p.split("\t")
    if prep[0] not in temp:
        print(id, "got one.")
        temp.append(prep[0])
        output_ppi.append(p)
    id += 1

print("filtering finished.\nsaving data...", end = "")

new_file = open(path + "output_ppi_2.txt", "w")
new_file.writelines(output_ppi)
new_file.close()

print("saved in", path + "output_ppi_2.txt.")
