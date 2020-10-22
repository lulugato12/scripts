# Unzip gene case data from GDC
# Lourdes B. Cajica
# 10 - 3 - 20

import os
import gzip

path = "C:/Users/hp/Desktop/redes_data/cerebro_data/"                           # path that contains the actual folder
count = 0
bad = list()                                                                    # this list save the non gzip file names

try:
    os.mkdir(path + "output/")                                                  # creates the folder where the data is going to be saved
except OSError as error:
    print("the folder already exists.")

print("Starting...")

for dir in os.listdir(path):                                                    # navigates through the folder of cases
    if not dir.endswith(".txt"):                                                # ignores the txt files
        print("file", count, "...", end = " ")
        for gz in os.listdir(path + dir + "/"):                                 # navigates through the case files
            if not gz.endswith(".txt"):                                         # ignores the txt files
                try:
                    input = gzip.GzipFile(path + dir + "/" + gz, "rb")          # unzip the case data
                    data = input.read()                                         # take the data
                    input.close()

                    output = open(path + "output/" + dir + ".txt", "wb")        # creates the txt file
                    output.write(data)                                          # save the data
                    output.close()
                except gzip.BadGzipFile:                                        # handles non valid gzip files
                    print("unvalid gzip...", end = " ")
                    bad.append(gz)                                              # save the bad files
        count += 1
        print("finished.")

if not len(bad) == 0:                                                           # if any bad file, saves it
    print("Saving bad files...")
    bfiles = open(path + "output/bad_files.txt", "w")
    bfiles.writelines(bad)
    bfiles.close()

print("Finished.")
print("saved in", path + "output/.")
