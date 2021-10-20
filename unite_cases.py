# Unite gene cases
# Lourdes B. Cajica
# Last update: 19 - 10 - 21

import os
import sys
import pandas as pd
from timer import Timer

path = 'C:/Users/hp/Desktop/mission_catness/'
count = 0
newlines = []
samples = os.listdir(path + "data/")
index = []

limit = False
max_found = 0                                       # count limit
if len(sys.argv) == 2:
    limit = True                                    # flag for giving an specific amount of samples
    max_found = int(sys.argv[1])
    print('Will be filtered', max_found, 'cases.')

with Timer("Reading data..."):
    for file in samples:                            # iterates through the directory files
        print("Reading file: " + file)
        data = open(path + "data/" + file, "r")     # open the current case file
        lines = data.readlines()                    # read all the lines
        data.close()

        i = 0
        for line in lines:                          # iterates through each line
            l = line.split('\t')
            if count == 0:                          # separates gene id and measure
                id = l[0].split('.')                # removes the gene version
                newlines.append([l[1].rstrip('\n')])
                index.append(id[0])
            else:
                newlines[i].append(l[1].rstrip('\n'))
                i += 1

        count += 1
        if limit and count == max_found:
            break

with Timer('Saving data...'):
    try:
        os.mkdir(path + 'output/')                  # creates the folder where the data is going to be saved
    except OSError as error:
        print('the folder already exists.')

    if limit:
        pd.DataFrame(newlines, columns = samples[:max_found], index = pd.Index(index)).to_csv(path + 'output/' + str(max_found) + '_cases.csv')
    else:
        pd.DataFrame(newlines, columns = samples, index = pd.Index(index)).to_csv(path + 'output/cases.csv')

print('Data saved in', path + 'output/cases.csv')
