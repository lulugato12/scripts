# Filter only protein coding genes
# Lourdes B. Cajica
# 20 - 3 - 21

# to create folder
import os

# requirements for resource measurement
import time
import resource

# creates an output folder it not exists
def create_folder(path):
    try:
        os.mkdir(path + "output/")                                      # creates the folder where the data is going to be saved
    except OSError as error:
        print("The folder already exists.", end = " ")

# reads the data from the files
def reading_data(protein_coding, cases):
    file_genes = open(protein_coding, "r")                              # opens the protein coding genes/proteins file
    file_cases = open(cases, "r")                                       # opens the cases file

    genes_data = file_genes.readlines()                                 # read the data
    cases_data = file_cases.readlines()                                 # read the data
    genes_unfiltered = genes_unfiltered[1:]                             # deletes the title line

    file_genes.close()
    file_cases.close()

    return genes_data, cases_data

# prepares the information
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

            if max_found:
                found += 1
        else:
            print("not found in genes.", end = " ")

        count += 1
        print("finished.")

        if limit and found <= max_found:
            break

    return filtered_genes, filtered_proteins

# saves the filtered data
def save_data(filtered_genes, filtered_proteins):
    file_output_genes = open(path + "output/genes.txt", "w")            # creates a file to save the cases output
    file_output_proteins = open(path + "output/proteins.txt", "w")      # creates a file to save the gene-protein data

    file_output_genes.writelines(filtered_genes)                        # saves the data
    file_output_proteins.writelines(filtered_proteins)                  # saves the data

    file_output_genes.close()
    file_output_proteins.close()

# variables
path = "/datos/ot/lbcajica/"                                            # path to the current directory
protein_coding = path + "datos/protein_coding.txt"                      # protein coding genes files
cases = path + "output/cases.txt"                                       # cases files

# limit setup
limit = True                                                            # boolean to find an specific amount of genes
max_found = 500                                                         # count limit

print("Creating new folder...", end = " ")
create_folder(path)

log = open(path + "log.txt", "a+")                                      # log file

print("finished.\nReading files...", end = " ")
@profile(presicion = 3, stream = log)
genes_data, cases_data = reading_data(protein_coding, cases)

print("finished.\nPreparing genes...", end = " ")
@profile(presicion = 3, stream = log)
genes, proteins = prep_data(genes_data)

print("finished.\nFiltering genes...")
@profile(presicion = 3, stream = log)
filtered_genes, filtered_proteins = filter_exec(cases_data, limit, max_found)

print("finished.\nSaving data...", end = " ")
save_data(filtered_genes, filtered_proteins)

print("Finished.\nGenes saved in " + path + "output/genes.txt.\nProteins saved in " + path + "output/proteins.txt.")
print("It took: ", time.thread_time()/60, "min\n")
log.write("Time execution:", time.thread_time()/60, "min\n")
