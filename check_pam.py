import pandas as pd

in_data = pd.read_csv("in_degree.csv", sep = "\t")
out_data = pd.read_csv("out_degree.csv", sep = "\t")
data = pd.read_csv("panda_total.csv", sep = "\t")

serie = data[:]["gene"]
genes = serie.drop_duplicates()

dummy = open("pam50.txt", "r").readlines()
pam50 = list()

print("Cleaning data...", end = " ")

for g in dummy:
    pam50.append(g.replace("\n",""))

print("Finished.\nFiltering found genes...", end = " ")

found = list()

for i in genes.index:
    if genes[i] in pam50:
        found.append(genes[i])

print("Finished.\nSaving force data...", end = " ")

filtered = list()

for i in data.index:
    if data["gene"][i] in pam50:
        filtered.append(data.iloc[i])

filtered = pd.DataFrame(filtered)

print("Finished.\nFound:", len(found))

for gene in found:
    print(gene + ":")
    filter = filtered["gene"] == gene
    out = filtered[filter]
    print(out)


filtered.to_csv(path_or_buf = "pam50_filtered.csv", sep = "\t")
