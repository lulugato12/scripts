# Filter PPI with the interested genes only
# Lourdes B. Cajica
# 10 - 25 - 20

import os
import time

path = "C:/Users/hp/Desktop/redes_data/"
proteins = list()
genes = list()
output_interactions = list()
count = 0

print("creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

print("finished.\nreading files...", end = "")

file_proteins = open(path + "output_proteins.txt", "r")
data_proteins = file_proteins.readlines()
file_proteins.close()

print("finished.\npreparing genes...", end = "")

for p in data_proteins:
    prep = p.split("\t")
    proteins.append(prep[1].rsplit("\n")[0])
    genes.append(prep[0].rsplit("\n")[0])

print("finished.\nfiltering genes...")

for file in os.listdir(path + "ppi/"):
    file_ppi = open(path + "ppi/" + file, "r")
    data_ppi = file_ppi.readlines()
    file_ppi.close()
    ppi = list()

    print("reading data...", end = "")
    for p in data_ppi:
        prep = p.split(" ")
        g1 = prep[0].split(".")
        g2 = prep[1].split(".")
        ppi.append([g1[1].rsplit("\n")[0], g2[1].rsplit("\n")[0]])

    print("finished. filtering...")

    for data in ppi:
        print("interaction", count, "...", end = "")
        if data[0] in proteins and data[1] in proteins:
            output_interactions.append(genes[proteins.index(data[0])] + "\t" + genes[proteins.index(data[1])] + "\t1.0\n")
            print("got one.", len(output_interactions))
            if len(output_interactions) == 500:
                break
        else:
            print("not found.", len(output_interactions))

        count += 1
        
        if len(output_interactions) == 500:
            break
    if len(output_interactions) == 500:
        break
    print("finished. sleeping...", end = "")
    time.sleep(20)
    print("ready!")

print("filtering finished.\nsaving data...", end = "")

new_file = open(path + "/output/output_ppi.txt", "w")
new_file.writelines(output_interactions)
new_file.close()

print("saved in", path + "output/output_ppi.txt.")
