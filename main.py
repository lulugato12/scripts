print("importando librerias...", end = "")
import os
from netZooPy.panda import Panda
from netZooPy.lioness import Lioness
from netZooPy.lioness.analyze_lioness import AnalyzeLioness
import pandas as pd

genes = 'C:/Users/hp/Desktop/redes_data/output_genes.txt'
ppi = 'C:/Users/hp/Desktop/redes_data/output_ppi.txt'
motif = 'C:/Users/hp/Desktop/redes_data/output_transcriptomes.txt'

print("finished. running pandas...")

panda_obj = Panda(genes, motif, ppi, remove_missing=False, keep_expression_matrix=True, save_memory=False)

print("finished.\nrunning lioness...")

lioness_obj = Lioness(panda_obj)
lioness_obj.save_lioness_results(file = 'lioness.txt')

print("finished.")
