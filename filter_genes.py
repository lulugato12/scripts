# Filter only protein coding genes
# Lourdes B. Cajica
# 15 - 3 - 21

import os

path = "C:/Users/hp/Desktop/redes_data/"
filtered_genes = list()
filtered_proteins = list()
proteins = list()
genes = list()

count = 0

print("Creating new folder...", end = " ")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = " ")

print("finished.\nReading files...", end = " ")

file_genes = open(path + "protein_coding.txt", "r")
file_cases = open(path + "output/cases.txt", "r")

genes_unfiltered = file_genes.readlines()
cases = file_cases.readlines()

file_genes.close()
file_cases.close()

genes_unfiltered = genes_unfiltered[1:]

print("finished.\nPreparing genes...", end = " ")

for gene in genes_unfiltered:
    prep = gene.split(",")
    genes.append(prep[0])
    if prep[1] != "\n":
        proteins.append(prep[1])
    else:
        proteins.append(" ")

print("finished.\nFiltering genes...")

for case in cases:
    print("gene ", count, "...", end = " ")
    c = case.split("\t")
    if c[0] in genes:
        filtered_genes.append(case)

        gene = genes[genes.index(c[0])]
        protein = proteins[genes.index(c[0])]
        if protein != " ":
            filtered_proteins.append(gene + "\t" + protein)
            print("got one.")
        else:
            print("not found in proteins.")
    else:
        print("not found in genes.")
    count += 1

print("finished.\nSaving data...", end = " ")

file_output_genes = open(path + "output/genes.txt", "w")
file_output_proteins = open(path + "output/proteins.txt", "w")

file_output_genes.writelines(filtered_genes)
file_output_proteins.writelines(filtered_proteins)

file_output_genes.close()
file_output_proteins.close()

print("Finished.\nGenes saved in", path + "output/genes.txt.\nProteins saved in", path + "output/proteins.txt.")
