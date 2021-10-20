# Unzip PPI interactions from STRING gz
# Lourdes B. Cajica
# Last update: 19 - 10 - 21

import os
import gzip
from timer import Timer

path = '#insert path here'
write_file = 'insert output file as .txt | ej: 9606.protein.links.v11.0.txt'
read_file = 'insert .gz file | ej. 9606.protein.links.v11.0.txt.gz'

with Timer("Unziping ppi data..."):
    try:
        txt = open(path + write_file, 'wb')
        gzfile = gzip.open(path + read_file, 'rb')
        txt.writelines(gzfile)
    except OSError as e:
        print("Not a valid .gz file :()")

print('Data saved in: ' + path + write_file)
