# Filter only protein coding genes
# Lourdes B. Cajica
# Last update: 19 - 10 - 21

import os
import sys
import pandas as pd
from timer import Timer

path = 'C:/Users/hp/Desktop/mission_catness/'       # path to the current directory
cases_data = pd.read_csv(path + 'output/250_cases.csv', index_col = 0)

file_genes = open(path + 'mart_export.txt', "r")
genes_data = file_genes.readlines()
genes_data = genes_data[1:]                         # deletes the title line
file_genes.close()

# limit setup
limit = False                                                           # boolean to find an specific amount of genes
max_found = 0                                                           # count limit
if len(sys.argv) == 2:
    limit = True                                                        # boolean to find an specific amount of genes
    max_found = int(sys.argv[1])                                        # count limit
    print('Will be filtered', max_found, 'genes.')

try:
    os.mkdir(path + 'output/')                  # creates the folder where the data is going to be saved
except OSError as error:
    print('the folder already exists.')

genes = list()

for gene in genes_data:
    prep = gene.split("\t")
    genes.append(prep[0])                   # saves the gene id

filtered_cases = list()                     # list that saves the filtered cases

count = 0
found = 0
x = 0

with Timer('Filtering data...'):
    for gene in cases_data.index:
        print('Checking for gene: ' + gene + "...", end = " ")

        if gene in genes:                                   # checks if the gene is protein coding
            if (cases_data.loc[gene] != 0).all():
                filtered_cases.append(cases_data.loc[gene]) # saves the cases associated to that gene
                print('got one.', end = ' ')
                found += 1

        else:
            print("not found in genes.", end = ' ')

        count += 1
        print('finished.')

        if limit and found > max_found:
            break

print('x:', x)
#with Timer('Saving data...'):
#    pd.DataFrame(filtered_cases, columns = cases_data.columns).to_csv(path + 'output/' + str(found) +'_cases.csv')
#    print('Cases saved in output/' + str(cases_data.index) +'_cases.csv')
