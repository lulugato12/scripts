#!/bin/bash

# script to prepare data for the lioness algorithm
echo "Preparing data for the lioness algorithm"

# download data
echo "Downloading data..."
sleep 2

mkdir datos
cd datos/
#wget https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
python \../scripts/download.py
cd ..

# unzip data 
echo "Starting unzip process..."
sleep 2

#python scripts/unzip_files.py
#python scripts/unite_cases.py
#python scripts/unzip_ppi.py

# removing trash
echo "Cleaning..."
sleep 2

#rm -rd data/
#rm -rd file/

# Preparing motif and PPI
echo "Filtering proteins..."
sleep 2
#python scripts/filter_genes.py

echo "Preparing motifs..."
sleep 2
#python scripts/filter_motifs.py

echo "Preparing PPI..."
sleep 2
#python scripts/filter_ppi.py

# 500 genes execution
echo "500 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 500

# LIONESS algorithm
echo "Executing lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

# 1000 genes execution
echo "1000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 1000

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

# 3000 genes execution
echo "3000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 3000

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."

# 5000 genes execution
echo "5000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 5000

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

# 10000 genes execution
echo "10000 genes execution"
sleep 2

# filter genes
echo "Starting genes filter process..."
sleep 2

python scripts/filter_genes.py 10000

# LIONESS execution
echo "Execution lioness..."
sleep 2

python scripts/main.py

echo "Finished lioness..."
sleep 2

# Last cleaning
echo "Cleaning..."
sleep 2

rm -rd datos/

echo "Process finished. Have a nice day :)"
