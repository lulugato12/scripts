# Unzip gene cases data from GDC
# Lourdes B. Cajica
# 15 - 3 - 21

import os
import xtarfile as tarfile

folder = "C:/Users/hp/Desktop/redes_data/"                      # base path
f = tarfile.open(folder + "protein.links.v11.0.txt.gz", 'r:gz') # unziping the .gz file
f.extractall(path = path)                                       # saving the data in the file/ folder
