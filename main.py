print("importando librerias...", end = "")
import os
from netZooPy.panda import Panda
from netZooPy.lioness import Lioness
from netZooPy.lioness.analyze_lioness import AnalyzeLioness
import pandas as pd

path = "/datos/ot/lbcajica/output"
genes = path + "genes.txt"
ppi = path + "ppi.txt"
motif = path + "motif.txt"

print("finished. running pandas...")

panda_obj = Panda(genes, motif, ppi, remove_missing=False, keep_expression_matrix=True, save_memory=False)

print("finished.\nrunning lioness...")

lioness_obj = Lioness(panda_obj)
lioness_obj.save_lioness_results(file = 'lioness.txt')

analyze_lioness_obj = AnalyzeLioness(lioness_obj)
analyze_lioness_obj.top_network_plot(top = 40, file = "lioness_top_40.png")

print("finished.")
