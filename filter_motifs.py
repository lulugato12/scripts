# change ids by its name
# Lourdes B. Cajica
# 15 - 3 - 21

import os
import time

path = "C:/Users/hp/Desktop/redes_data/"
tf_name = list()
gene_name = list()
tf_id = list()
gene_id = list()
output = list()

print("Creating new folder...", end=" ")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = "")

print("finished.\nReading files...", end = " ")

file_motif = open(path + "ToyMotifData.txt", "r")
original = file_motif.readlines()
file_motif.close()

file_names = open(path + "mart_export.txt", "r")
update = file_names.readlines()
file_names.close()

print("finished.\nPreparing data...", end = " ")

for l in update:
    line = l.split("\t")
    gene_id.append(line[0])
    tf_id.append(line[1])
    gene_name.append(line[2])
    tf_name.append(line[3].split("\n")[0])

print("finished.\nFiltering names...")
i = 0
for p in original:
    print("line", i)
    prep = p.split("\t")
    line = ""
    if prep[0] in gene_name and prep[1] in gene_name:
        line += tf_id[gene_name.index(prep[0])] + "\t" + gene_id[gene_name.index(prep[1])] + "\t1.0\n"
    if output != "":
        output.append(line)
    i += 1

print("finished.\nSaving data...", end = " ")

new_file = open(path + "output/motif.txt", "w")
new_file.writelines(output)
new_file.close()

print("finished.\nData saved in", path + "motif.txt.")
