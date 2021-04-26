# requirements for resource monitoring
import time
import resource
from memory_profiler import profile

# NetZooPy requirements
from netZooPy.panda import Panda
from netZooPy.lioness import Lioness
from netZooPy.lioness.analyze_lioness import AnalyzeLioness
import pandas as pd

# variables definition
path = "/datos/ot/lbcajica/"                                                        # base path to the data folder
log = open(path + "log.txt", "a+")                                                  # log file
genes = path + "output/genes.txt"                                                   # genes file
motif = path + "output/motif.txt"                                                   # motif file
ppi = path + "output/ppi.txt"                                                       # ppi file
nodes = 40                                                                          # amount of nodes for the final plot
RAM_max = 40                                                                        # RAM max value in Gigabytes

log.write("LIONESS\n")

# function to execute the PANDA algorithm
#@profile(precision = 3, stream = log)
def panda_exec(genes, motif, ppi):
    panda_obj = Panda(genes, None, ppi, remove_missing=False, keep_expression_matrix=True, save_memory=False)
    return panda_obj

# function to execute the pipeline of the LIONESS algorithm
#@profile(precision = 3, stream = log)
def lioness_exec(panda_obj, nodes):
    lioness_obj = Lioness(panda_obj)                                                # LIONESS object generator
    lioness_obj.save_lioness_results(file = 'lioness.txt')                          # store the LIONESS data

# function to set a limit of RAM resource
def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

try:
    limit_memory(RAM_max * 1024 * 1024 * 1024)                                      # RAM max_limit | 40 G

    print("Running pandas...")
    panda_obj = panda_exec(genes, motif, ppi)

    print("finished.\nRunning lioness...")
    lioness_exec(panda_obj, nodes)

    print("finished. It took", time.thread_time()/60, "min")                        # time execution
    log.write("Time execution:" + str(time.thread_time()/60) + "min\n")
except MemoryError:                                                                 # rised error due to RAM limit
    print("Memory exceeded :(")
    log.write("Memory exceeded :(.\n")

log.close()
