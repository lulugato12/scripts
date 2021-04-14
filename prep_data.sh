#!/bin/bash

# script to prepare data for the lioness algorithm
echo "LIONESS EXECUTION"

# download data
#wget https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

# 500 genes execution
echo "3000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 3000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif filter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS algorithm
echo "Executing lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness3000
mv lioness_output/ lioness3000/
mv lioness_top_40.png lioness3000/

# 5000 genes execution
echo "1000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 5000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif silter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness5000
mv lioness_output/ lioness5000/
mv lioness_top_40.png lioness5000/

# 500 genes execution
echo "8000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 8000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif filter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS algorithm
echo "Executing lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness8000
mv lioness_output/ lioness8000/
mv lioness_top_40.png lioness8000/

# 1000 genes execution
echo "1000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 10000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif silter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness10000
mv lioness_output/ lioness10000/
mv lioness_top_40.png lioness10000/

# 13000 genes execution
echo "13000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 13000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif filter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS algorithm
echo "Executing lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness13000
mv lioness_output/ lioness13000/
mv lioness_top_40.png lioness13000/

# 1000 genes execution
echo "15000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 15000

echo "Starting ppi filter process..."
sleep 2

python scripts/filter_ppi.py

echo "Starting motif silter process..."
sleep 2

python scripts/filter_motifs.py

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

mkdir lioness15000
mv lioness_output/ lioness15000/
mv lioness_top_40.png lioness15000/

echo "Process finished. Have a nice day :)"