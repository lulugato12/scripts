# Unite gene cases
# Lourdes B. Cajica
# 10 - 3 - 20

import os

path = "C:/Users/hp/Desktop/redes_data/cerebro_data/output/"                    # the path to the directory
count = 0
newlines = list()

for file in os.listdir(path):                                                   # iterates through the directory files
    print("file", count, "...", end = "")
    data = open(path + file, "r")                                               # open the current case file
    lines = data.readlines()                                                    # read all the lines
    data.close()

    i = 0
    for line in lines:                                                          # iterates through each line
        if count == 0:
            l = line.split("\t")                                                # separates gene id and measure
            id = l[0].split(".")                                                # separates the gene version
            newlines.append("\n" + id[0] + "\t" + l[1].rstrip("\n"))            # save the new line
        else:
            l = line.split("\t")                                                # separates gene id and measure
            newlines[i] += "\t" + l[1].rstrip("\n")                             # saves the measure only
            i += 1

    count += 1
    print(" finished.")

print("writing final file...", end = "")

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

newlines[0] = newlines[0].replace("\n", "")                                     # deletes the \n in the line

newfile = open(path + "output/output.txt", "w")                                 # creates the output file
newfile.writelines(newlines)                                                    # writes down the data
newfile.close()

print(" finished.")
print("saved in", path + "output/output.txt.")
