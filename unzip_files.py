# Unzip gene cases data from GDC
# Lourdes B. Cajica
# Last update: 19 - 10 - 21

import os
import gzip
import xtarfile as tarfile
from timer import Timer

path = 'insert path'
read_file = 'insert .gz file | ej. gdc_download_20211006_173713.629179.tar.gz'

with Timer("Creting folders..."):
    try:
        os.mkdir(path + "file/")            # creates the folder for the unzipped folders
        os.mkdir(path + "data/")            # creates the folder where the data is going to be saved
    except OSError as error:
        print("the folders already exists.")

with Timer("Unziping folder..."):
    f = tarfile.open(read_file, 'r:gz')     # unziping the .gz file
    f.extractall(path = path + "file/")     # saving the data in the file/ folder

with Timer("Starting extraction..."):
    for dir in os.listdir(path + "file/"):              # navigates through the folder of cases
        if not dir.endswith(".txt"):                    # ignores the txt files
            print("Extracting :" + dir + "...")
            for gz in os.listdir(path + "file/" + dir + "/"):           # navigates through the case files
                if not gz.endswith(".txt"):                             # ignores the txt files
                    try:
                        txt = open(path + "data/" + dir + ".txt", 'wb')             # new .txt files
                        gzfile = gzip.open(path + "file/" + dir + "/" + gz, 'rb')   # zipped folder
                        txt.writelines(gzfile)
                    except OSError as e:
                        print("Not a valid .gz file")

print('Data saved in' + path + 'data/')
