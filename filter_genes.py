# Filter only protein coding genes
# Lourdes B. Cajica
# 15 - 3 - 21

import os

path = "C:/Users/hp/Desktop/redes_data/"                                # path to the current directory
filtered_genes = list()                                                 # list that save the filtered genes
filtered_proteins = list()                                              # list that saves the filtered proteins
proteins = list()                                                       # list that saves general proteins
genes = list()                                                          # list that saves general genes

count = 0

print("Creating new folder...", end = " ")

try:
    os.mkdir(path + "output/")                                          # creates the folder where the data is going to be saved
except OSError as error:
    print("The folder already exists.", end = " ")

print("finished.\nReading files...", end = " ")

file_genes = open(path + "protein_coding.txt", "r")                     # opens the protein coding genes/proteins file
file_cases = open(path + "output/cases.txt", "r")                       # opens the cases file

genes_unfiltered = file_genes.readlines()                               # read the data
cases = file_cases.readlines()                                          # read the data

file_genes.close()
file_cases.close()

genes_unfiltered = genes_unfiltered[1:]                                 # deletes the title line

print("finished.\nPreparing genes...", end = " ")

for gene in genes_unfiltered:
    prep = gene.split(",")                                              # splits the data line
    genes.append(prep[0])                                               # saves the gene id
    if prep[1] != "\n":
        proteins.append(prep[1])                                        # if protein, saves the protein id
    else:
        proteins.append(" ")

print("finished.\nFiltering genes...")

for case in cases:
    print("gene ", count, "...", end = " ")
    c = case.split("\t")                                                # splits the data line
    if c[0] in genes:                                                   # checks if the gene is protein coding
        filtered_genes.append(case)                                     # saves the cases associated to that gene

        gene = genes[genes.index(c[0])]                                 # searches for the gene id
        protein = proteins[genes.index(c[0])]                           # searches for a protein associated to that gene
        if protein != " ":
            filtered_proteins.append(protein)                           # if a protein, saves the protein to another list
            print("got one.")
        else:
            print("not found in proteins.")
    else:
        print("not found in genes.")
    count += 1

print("finished.\nSaving data...", end = " ")

file_output_genes = open(path + "output/genes.txt", "w")                # creates a file to save the cases output
file_output_proteins = open(path + "output/proteins.txt", "w")          # creates a file to save the gene-protein data

file_output_genes.writelines(filtered_genes)                            # saves the data
file_output_proteins.writelines(filtered_proteins)                      # saves the data

file_output_genes.close()
file_output_proteins.close()

print("Finished.\nGenes saved in", path + "output/genes.txt.\nProteins saved in", path + "output/proteins.txt.")
