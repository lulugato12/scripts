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

file_proteins = open(path + "proteins.txt", "r")
data_proteins = file_proteins.readlines()
file_proteins.close()

print("finished.\npreparing genes...", end = "")

for p in data_proteins:
    prep = p.split("\t")
    proteins.append(prep[1].rsplit("\n"))
    genes.append(prep[0].rsplit("\n"))

print("finished.\nfiltering genes...")

for file in os.listdir(path + "ppi_interactions/"):
    file_ppi = open(path + "ppi_interactions/" + file, "r")
    data_ppi = file_ppi.readlines()
    file_ppi.close()
    ppi = list()

    for p in data_ppi:
        prep = p.split(" ")
        g1 = prep[0].split(".")
        g2 = prep[1].split(".")
        ppi.append([g1[1].rsplit("\n"), g2[1].rsplit("\n")])

    for data in ppi:
        print("interaction", count, "...", end = "")
        if data[0] in proteins and data[1] in proteins:
            output_interactions.append(genes[proteins.find(data[0])] + "\t" + genes[proteins.find(data[1])] + "\t1.0\n")
            print("got one.")
        else:
            print("not found.")
        count += 1

    print("sleeping...", end = "")
    time.sleep(20)
    print("ready!")

print("filtering finished.\nsaving data...", end = "")

new_file = open(path + "/output/ppi_interactions.txt", "w")
new_file.writelines(output_interactions)
new_file.close()

print("saved in", path + "output/ppi_interactions.txt.")
