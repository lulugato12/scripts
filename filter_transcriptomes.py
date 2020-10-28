# Filter only transcriptomes from interested genes
# Lourdes B. Cajica
# 10 - 3 - 20

import os

path = "C:/Users/hp/Desktop/redes_data/"
genes = list()
filtered = list()
transcriptomes = list()
count = 0

print("creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

print("finished.\nreading files...", end = "")

file_data = open(path + "transcriptomes.txt", "r")
file_cases = open(path + "output_genes.txt", "r")

transcriptomes_unfiltered = file_data.readlines()
cases = file_cases.readlines()

file_data.close()
file_cases.close()

print("finished.\npreparing genes...", end = "")

for t in transcriptomes_unfiltered:
    prep = t.split(",")
    genes.append(prep[0].rsplit("\n")[0])
    transcriptomes.append(prep[1].rsplit("\n")[0])

print("finished.\nfiltering genes...")

for case in cases:
    print("gene ", count, "...", end = " ")
    c = case.split("\t")

    if c[0].rsplit("\n")[0] in genes:
        print("got one.")
        value = transcriptomes[genes.index(c[0])]
        filtered.append(value + "\t" + c[0] + "\t" + "1\n")
    else:
        print("not found in genes.")

    count += 1

print("finished. saving data...", end = "")

file_output_transcriptomes = open(path + "output/output_transcriptomes.txt", "w")

file_output_transcriptomes.writelines(filtered)

file_output_transcriptomes.close()

print("finished.")
print("transcriptomes saved in", path + "output/output_transcriptomes.txt.")
