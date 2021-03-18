# change ids by its name
# Lourdes B. Cajica
# 15 - 3 - 21

import os
import time

path = "/datos/ot/lbcajica/"                                            # path to the current directory
tf_name = list()                                                        # list of motif names
gene_name = list()                                                      # list of gene names
tf_id = list()                                                          # list of motif ids
gene_id = list()                                                        # list of gene ids
output = list()                                                         # output data lines
count = 0

print("Creating new folder...", end=" ")

try:
    os.mkdir(path + "output/")                                          # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = "")

print("finished.\nReading files...", end = " ")

file_motif = open(path + "datos/ToyMotifData.txt", "r")                 # opens the file that contains the motif data
original = file_motif.readlines()                                       # reads all the data
file_motif.close()

file_names = open(path + "datos/mart_export.txt", "r")                  # opens the file that contians the name-id relation
update = file_names.readlines()                                         # reads all the data
file_names.close()

print("finished.\nPreparing data...", end = " ")

for l in update:
    line = l.split("\t")                                                # splits the data line
    gene_id.append(line[0])                                             # saves de gene id
    tf_id.append(line[1])                                               # saves the motif id
    gene_name.append(line[2])                                           # saves the gene name
    tf_name.append(line[3].split("\n")[0])                              # saves the motif name

print("finished.\nFiltering names...")

for p in original:
    print("line " + str(count) + "...", end = " ")
    prep = p.split("\t")                                                # splits the data line to get the motif and the gene
    line = ""
    if prep[0] in gene_name and prep[1] in gene_name:                   # check if both the motif and the gene exists in the registries
        print("got one.", end = " ")
        line += tf_id[gene_name.index(prep[0])] + "\t" + gene_id[gene_name.index(prep[1])] + "\t1.0\n"
        output.append(line)                                             # saves the motif id, the gene id and the weight 1.0
    count += 1
    print("finished.")

print("finished.\nSaving data...", end = " ")

new_file = open(path + "output/motif.txt", "w")                         # creates a new file to save the motifs
new_file.writelines(output)                                             # saves the data
new_file.close()

print("finished.\nData saved in " + path + "motif.txt.")
