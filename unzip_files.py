# Unzip gene cases data from GDC
# Lourdes B. Cajica
# 15 - 3 - 21

import os
import gzip
import xtarfile as tarfile

path = "/datos/ot/lbcajica/"                                             # path that contains the actual folder
folder = path + "datos/breast_data.gz"                                 # initial .gz file
count = 0
bad = list()                                                            # this list saves the non .gz file names

print("Creating folders...", end = " ")

try:
    os.mkdir(path + "file/")                                            # creates the folder for the unzipped folders
    os.mkdir(path + "data/")                                            # creates the folder where the data is going to be saved
except OSError as error:
    print("the folders already exists.")

print("finished.\nUnziping folder...", end = " ")

f = tarfile.open(folder, 'r:gz')                                        # unziping the .gz file
f.extractall(path = path + "file/")                                     # saving the data in the file/ folder

print("finished.\nStarting extraction.")

for dir in os.listdir(path + "file/"):                                  # navigates through the folder of cases
    if not dir.endswith(".txt"):                                        # ignores the txt files
        print("file " + str(count) + "...", end = " ")
        for gz in os.listdir(path + "file/" + dir + "/"):               # navigates through the case files
            if not gz.endswith(".txt"):                                 # ignores the txt files
                try:
                    txt = open(path + "data/" + dir + ".txt", 'wb')             # new .txt files
                    gzfile = gzip.open(path + "file/" + dir + "/" + gz, 'rb')   # zipped folder
                    txt.writelines(gzfile)
                except OSError as e:                                            # if something goes wrong
                    print("Not a valid .gz file")
                    bad.append(gz)
        count += 1
        print("finished.")

if len(bad) != 0:                                                       # if any bad file, saves it
    try:
        os.mkdir(path + "badfiles/")                                    # creates the folder with the bad data
    except OSError as error:
        print("the folder already exists.")

    print("Saving bad files...")
    bfiles = open(path + "badfiles/output.txt", "w")                    # creates a new file
    bfiles.writelines(bad)                                              # stores the data
    bfiles.close()

print("finished.\nSaved data in " + path + "data/")
