# change ids by its name
# Lourdes B. Cajica
# 20 - 3 - 21

# to create folder
import os

# requirements for resource measurement
import time
import resource
from memory_profiler import profile

# creates an output folder it not exists
def create_folder(path):
    try:
        os.mkdir(path + "output/")                                      # creates the folder where the data is going to be saved
    except OSError as error:
        print("The folder already exists.", end = " ")

# reads the data from the files
def reading_data(motifs, updates):
    file_motif = open(motifs, "r")                                      # opens the file that contains the motif data
    file_names = open(updates, "r")                                     # opens the file that contians the name-id relation

    original = file_motif.readlines()                                   # reads all the data
    update = file_names.readlines()                                     # reads all the data

    file_names.close()
    file_motif.close()

    return original, update

# prepares the information
def prep_data(update):
    # storage
    tf_name = list()                                                    # list of motif names
    gene_name = list()                                                  # list of gene names
    tf_id = list()                                                      # list of motif ids
    gene_id = list()                                                    # list of gene ids

    for l in update:
        line = l.split("\t")                                            # splits the data line
        gene_id.append(line[0])                                         # saves de gene id
        tf_id.append(line[1])                                           # saves the motif id
        gene_name.append(line[2])                                       # saves the gene name
        tf_name.append(line[3].split("\n")[0])                          # saves the motif name

    return gene_id, ft_id, gene_name, tf_name

# executes the filtering process
def filter_exec(gene_id, ft_id, gene_name, tf_name):
    # variables
    output = list()                                                     # output data lines
    count = 0

    for p in original:
        print("line " + str(count) + "...", end = " ")
        prep = p.split("\t")                                            # splits the data line to get the motif and the gene
        line = ""
        if prep[0] in gene_name and prep[1] in gene_name:               # check if both the motif and the gene exists in the registries
            print("got one.", end = " ")
            line += tf_id[gene_name.index(prep[0])] + "\t" + gene_id[gene_name.index(prep[1])] + "\t1.0\n"
            output.append(line)                                         # saves the motif id, the gene id and the weight 1.0
        count += 1
        print("finished.")

    return output

# saves the filtered data
def save_data(output):
    new_file = open(path + "output/motif.txt", "w")                     # creates a new file to save the motifs
    new_file.writelines(output)                                         # saves the data
    new_file.close()

# variables
path = "/datos/ot/lbcajica/"                                            # path to the current directory
motifs = path + "datos/ToyMotifData.txt"                                # motif file
updates = path + "datos/mart_export.txt"                                # ids file

print("Creating new folder...", end=" ")
create_folder()
log = open(path + "log.txt", "a+")                                      # log file

print("finished.\nReading files...", end = " ")
@profile(presicion = 3, stream = log)
original, update = reading_data(motifs, updates)

print("finished.\nPreparing data...", end = " ")
@profile(presicion = 3, stream = log)
gene_id, ft_id, gene_name, tf_name = prep_data(update)

print("finished.\nFiltering names...")
@profile(presicion = 3, stream = log)
output = filter_exec(gene_id, ft_id, gene_name, tf_name)

print("finished.\nSaving data...", end = " ")
save_data(output)

print("finished.\nData saved in " + path + "motif.txt.")
print("It took: ", time.thread_time()/60, "min\n")
log.write("Time execution:", time.thread_time()/60, "min\n")
