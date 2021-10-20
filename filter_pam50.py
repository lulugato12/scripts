# Filtering the samples that belongs to the PAM50 set
# Lourdes B. Cajica
# Last update: 19 - 10 - 21

import pandas as pd
from timer import Timer

path = 'C:/Users/hp/Desktop/mission_catness/'
output = []

file_pam50 = open(path + 'pam50.txt', 'r')
pam50 = [i.replace('\n', '') for i in file_pam50.readlines()]
file_pam50.close()

cases_data = pd.read_csv(path + 'output/15_cases.csv', index_col = 0)

with Timer('Looking for PAM50...'):
    for gene in cases_data.index:
        print('Checking gene: ' + gene)
        if gene in pam50:
            output.append(cases_data.loc[gene])

    pd.DataFrame(output, index = pd.Index(pam50)).to_csv(path + 'output/cases_pam50.csv')

print('Data saved in output/cases_pam50.csv')
