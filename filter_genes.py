# Filter only protein coding genes
# Lourdes B. Cajica
# 20 - 3 - 21

# to create folder and get parameters
import os
import sys

# requirements for resource measurement
import time
import resource
from memory_profiler import profile

# variables
path = "/datos/ot/lbcajica/"                                            # path to the current directory
log = open(path + "log.txt", "a+")                                      # log file
protein_coding = path + "datos/protein_coding.txt"                      # protein coding genes files
cases = path + "output/cases.txt"                                       # cases files

log.write("Filter genes.\n")

# limit setup
limit = False                                                           # boolean to find an specific amount of genes
max_found = 0                                                           # count limit
if len(sys.argv) == 2:
    limit = True                                                        # boolean to find an specific amount of genes
    max_found = int(sys.argv[1])                                        # count limit
    print("Will be filtered", max_found, "genes.", end = " ")

# creates an output folder it not exists
def create_folder(path):
    try:
        os.mkdir(path + "output/")                                      # creates the folder where the data is going to be saved
    except OSError as error:
        print("The folder already exists.", end = " ")

# reads the data from the files
#@profile(precision = 3, stream = log)
def reading_data(protein_coding, cases):
    file_genes = open(protein_coding, "r")                              # opens the protein coding genes/proteins file
    file_cases = open(cases, "r")                                       # opens the cases file

    genes_data = file_genes.readlines()                                 # read the data
    cases_data = file_cases.readlines()                                 # read the data
    genes_data = genes_data[1:]                                         # deletes the title line

    file_genes.close()
    file_cases.close()

    return genes_data, cases_data

# prepares the information
#@profile(precision = 3, stream = log)
def prep_data(genes_data):
    # storage variables
    genes = list()
    proteins = list()

    for gene in genes_data:
        prep = gene.split(",")                                          # splits the data line
        genes.append(prep[0])                                           # saves the gene id
        if prep[1] != "\n":
            proteins.append(prep[1])                                    # if protein, saves the protein id
        else:
            proteins.append(" ")                                        # if no protein, leaves it blank

    return genes, proteins

# executes the filtering process
#@profile(precision = 3, stream = log)
def filter_exec(cases_data, limit, max_found):
    # storage variables
    filtered_genes = list()                                             # list that save the filtered genes
    filtered_proteins = list()                                          # list that saves the filtered proteins

    # counter
    count = 0
    found = 0

    for case in cases_data:
        print("gene " + str(count) + "...", end = " ")
        c = case.split("\t")                                            # splits the data line

        if c[0] in genes:                                               # checks if the gene is protein coding
            filtered_genes.append(case)                                 # saves the cases associated to that gene
            gene = genes[genes.index(c[0])]                             # searches for the gene id
            protein = proteins[genes.index(c[0])]                       # searches for a protein associated to that gene
            print("got one.", end = " ")

            if protein != " ":
                filtered_proteins.append(protein)                       # if a protein, saves the protein to another list

            if limit:
                found += 1
        else:
            print("not found in genes.", end = " ")

        count += 1
        print("finished.")

        if limit and found > max_found:
            break

    return filtered_genes, filtered_proteins

# saves the filtered data
#@profile(precision = 3, stream = log)
def save_data(filtered_genes, filtered_proteins):
    file_output_genes = open(path + "output/genes.txt", "w")            # creates a file to save the cases output
    file_output_proteins = open(path + "output/proteins.txt", "w")      # creates a file to save the gene-protein data

    file_output_genes.writelines(filtered_genes)                        # saves the data
    file_output_proteins.writelines(filtered_proteins)                  # saves the data

    file_output_genes.close()
    file_output_proteins.close()

print("Creating new folder...", end = " ")
create_folder(path)

print("finished.\nReading files...", end = " ")
genes_data, cases_data = reading_data(protein_coding, cases)

print("finished.\nPreparing genes...", end = " ")
genes, proteins = prep_data(genes_data)

print("finished.\nFiltering genes...")
filtered_genes, filtered_proteins = filter_exec(cases_data, limit, max_found)

print("finished.\nSaving data...", end = " ")
save_data(filtered_genes, filtered_proteins)

print("Finished.\nGenes saved in " + path + "output/genes.txt.\nProteins saved in " + path + "output/proteins.txt.")
print("It took: ", time.thread_time()/60, "min\n")

log.write("Time execution:" + str(time.thread_time()/60) + "min\n")
log.close()
