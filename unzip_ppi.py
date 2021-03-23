# Unzip PPI interactions from STRING gz
# Lourdes B. Cajica
# 17 - 3 - 21

import os
import gzip

path = "/datos/ot/lbcajica/"                                                # base path

print("Starting unziping ppi data...", end = " ")

try:
    txt = open(path + "datos/9606.protein.links.v11.0.txt", 'wb')                # new .txt files
    gzfile = gzip.open(path + "datos/9606.protein.links.v11.0.txt.gz", 'rb')     # zipped folder
    txt.writelines(gzfile)                                                  # final file
except OSError as e:                                                        # if something goes wrong
    print("Not a valid .gz file")

print("finished.\n Data saved in " + path + "datos/protein.links.v11.0.txt")
