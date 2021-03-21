# requirements for resource monitoring
import time
import resource

# NetZooPy requirements
from netZooPy.panda import Panda
from netZooPy.lioness import Lioness
from netZooPy.lioness.analyze_lioness import AnalyzeLioness
import pandas as pd

# function to execute the pipeline of the LIONESS algorithm
def lioness_exec(panda_obj, nodes):
    lioness_obj = Lioness(panda_obj)                                                # LIONESS object generator
    lioness_obj.save_lioness_results(file = 'lioness.txt')                          # store the LIONESS data

    analyze_lioness_obj = AnalyzeLioness(lioness_obj)                               # network generator
    analyze_lioness_obj.top_network_plot(top = nodes, file = "lioness_top_40.png")  # plot generator up to X nodes

# function to set a limit of RAM resource
def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

# variables definition
path = "/datos/ot/lbcajica/output/"                                                 # base path to the data folder
log = open(path + "log.txt", "a+")                                                  # log file
genes = path + "genes.txt"                                                          # genes file
ppi = path + "ppi.txt"                                                              # ppi file
motif = path + "motif.txt"                                                          # motif file
nodes = 40                                                                          # amount of nodes for the final plot
RAM_max = 40                                                                        # RAM max value in Gigabytes

try:
    limit_memory(RAM_max * 1024 * 1024 * 1024)                                      # RAM max_limit | 40 G

    print("Running pandas...")
    @profile(presicion = 3, stream = log)
    panda_obj = Panda(genes, motif, ppi, remove_missing=False, keep_expression_matrix=True, save_memory=False)

    print("finished.\nRunning lioness...")
    @profile(presicion = 3, stream = log)
    lioness_exec(panda_obj, nodes)

    print("finished. It took", time.thread_time()/60, "min")                        # time execution
except MemoryError:                                                                 # rised error due to RAM limit
    print("Memory exceeded :(")
    log.write("Memory exceeded :(.\n")
