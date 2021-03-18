# Clean PPI with ids and weight
# Lourdes B. Cajica
# 18 - 3 - 21

import os
import time

path = "C:/Users/hp/Desktop/redes_data/"                                # path to the current directory
output_interactions = list()                                            # list that stores the ppi data
count = 0

print("Creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                          # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = " ")

print("finished.\nReading files...", end = "")

file_ppi = open(path + "9606.protein.links.v11.0.txt", "r")             # opens the file that contiains the protein interactions
data_ppi = file_ppi.readlines()                                         # reads the data
file_ppi.close()

file_proteins = open(path + "output/genes.txt", "r")                    # opens the file that contains the proteins
data_proteins = file_proteins.readlines()                               # reads the data
file_proteins.close()

print("finished.\nFiltering PPI...")

for line in data_ppi:
     l = line.split("\t")                                               # splits the data line
     p1 = l[0].split(".")[1]                                            # reads the first protein
     p2 = l[1].split(".")[1]                                            # reads the second protein
     w = "0." + l[3].split("\n")[0]                                     # reads the interaction weight

     if l[0] + "\n" in data_proteins and l[1] + "\n" in data_proteins:
         output_interactions.append(p1 + "\t" + p2 + "\t" + w + "\n")   # saves the data

print("finished.\nSaving data...", end = "")

new_file = open(path + "/output/ppi.txt", "w")                          # creates a new file to save the data
new_file.writelines(output_interactions)                                # saves the data
new_file.close()

print("finished.\nData saved in", path + "output/ppi.txt.")
