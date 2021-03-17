# Unzip PPI interactions from STRING gz
# Lourdes B. Cajica
# 17 - 3 - 21

import os
import gzip

path = "C:/Users/hp/Desktop/redes_data/"                                # base path
try:
    txt = open(path + "data/protein.links.v11.0.txt", 'wb')             # new .txt files
    gzfile = gzip.open(path + "file/protein.links.v11.0.txt.gz", 'rb')  # zipped folder
        txt.writelines(gzfile)                                          # final file
except gzip.BadGzipFile as e:                                           # if something goes wrong
    print("Not a valid .gz file")
