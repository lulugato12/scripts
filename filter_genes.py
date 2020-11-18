# Filter only protein coding genes
# Lourdes B. Cajica
# 10 - 3 - 20

import os

path = "C:/Users/hp/Desktop/redes_data/"
genes = list()
filtered_genes = list()
filtered_proteins = list()
proteins = list()
count = 0

print("creating new folder...", end="")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

print("finished.\nreading files...", end = "")

file_genes = open(path + "protein_coding.txt", "r")
file_cases = open(path + "genes_cerebro.txt", "r")

genes_unfiltered = file_genes.readlines()
cases = file_cases.readlines()

file_genes.close()
file_cases.close()

genes_unfiltered = genes_unfiltered[1:]

print("finished.\npreparing genes...", end = "")

for gene in genes_unfiltered:
    prep = gene.split(",")
    genes.append(prep[0])
    if len(prep) == 2:
        proteins.append(prep[1])
    else:
        proteins.append(" ")

print("finished.\nfiltering genes...")

for case in cases:
    print("gene ", count, "...", end = " ")
    c = case.split("\t")
    if c[0] in genes:
        print("got one.")
        filtered_genes.append(case)

        gene = genes[genes.index(c[0])]
        value = proteins[genes.index(c[0])]
        if value != " ":
            filtered_proteins.append(gene + "\t" + value)
    else:
        print("not found in genes.")
    count += 1

file_output_genes = open(path + "output/output_genes.txt", "w")
file_output_proteins = open(path + "output/output_proteins.txt", "w")

file_output_genes.writelines(filtered_genes)
file_output_proteins.writelines(filtered_proteins)

file_output_genes.close()
file_output_proteins.close()

print("finished.")
print("genes saved in", path + "output/output_genes.txt.")
print("proteins saved in", path + "output/output_proteins.txt.")
