# Unite gene cases
# Lourdes B. Cajica
# 15 - 3 - 21

import os

path = "C:/Users/hp/Desktop/redes_data/"                                # the path to the directory
count = 0
newlines = list()

print("Reading data...", end = " ")

for file in os.listdir(path + "data/"):                                 # iterates through the directory files
    print("file", count, "...", end = "")
    data = open(path + "data/" + file, "r")                             # open the current case file
    lines = data.readlines()                                            # read all the lines
    data.close()

    i = 0
    for line in lines:                                                  # iterates through each line
        if count == 0:
            l = line.split("\t")                                        # separates gene id and measure
            id = l[0].split(".")                                        # separates the gene version
            newlines.append("\n" + id[0] + "\t" + l[1].rstrip("\n"))    # save the new line
        else:
            l = line.split("\t")                                        # separates gene id and measure
            newlines[i] += "\t" + l[1].rstrip("\n")                     # saves the measure only
            i += 1

    count += 1
    print(" finished.")

print("finished.\nWriting final file...", end = " ")

try:
    os.mkdir(path + "output/")                                          # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

newlines[0] = newlines[0].replace("\n", "")                             # deletes the \n in the line

newfile = open(path + "output/cases.txt", "w")                          # creates the output file
newfile.writelines(newlines)                                            # writes down the data
newfile.close()

print("finished.\nData saved in", path + "output/cases.txt.")
