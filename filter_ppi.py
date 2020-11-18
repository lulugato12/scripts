# Clean PPI with ids and weight
# Lourdes B. Cajica
# 11 - 18 - 20

import os
import time

path = "C:/Users/hp/Desktop/redes_data/"
output_interactions = list()
count = 0

print("creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists...", end = "")

print("finished.\nreading files...", end = "")

file_proteins = open(path + "string_interactions.tsv", "r")
data_proteins = file_proteins.readlines()
file_proteins.close()

print("finished.\ncleaning PPI...")

for line in data_proteins:
     l = line.split("\t")
     p1 = l[2].split(".")[1]
     p2 = l[3].split(".")[1]
     w = l[12].split("\n")[0]
     output_interactions.append(p1 + "\t" + p2 + "\t" + w + "\n")

print("finished.\nsaving data...", end = "")

new_file = open(path + "/output/output_ppi.txt", "w")
new_file.writelines(output_interactions)
new_file.close()

print("saved in", path + "output/output_ppi.txt.")
