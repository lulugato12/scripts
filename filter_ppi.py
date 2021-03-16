# Clean PPI with ids and weight
# Lourdes B. Cajica
# 11 - 18 - 20

import os
import time

path = "C:/Users/hp/Desktop/redes_data/"                                # path to the current directory
output_interactions = list()                                            # list that saves the ppi data
count = 0

print("Creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                          # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = " ")

print("finished.\nReading files...", end = "")

file_proteins = open(path + "string_interactions.tsv", "r")             # opens the file that contiains the protein interactions
data_proteins = file_proteins.readlines()                               # reads the data
file_proteins.close()

print("finished.\nCleaning PPI...")

for line in data_proteins:
     l = line.split("\t")                                               # splits the data line
     p1 = l[2].split(".")[1]                                            # saves the first protein
     p2 = l[3].split(".")[1]                                            # saves the second protein
     w = l[12].split("\n")[0]                                           # saves the interaction weight
     output_interactions.append(p1 + "\t" + p2 + "\t" + w + "\n")       # sabes the data

print("finished.\nSaving data...", end = "")

new_file = open(path + "/output/ppi.txt", "w")                          # creates a new file to save the data
new_file.writelines(output_interactions)                                # saves the data
new_file.close()

print("finished.\nData saved in", path + "output/ppi.txt.")
