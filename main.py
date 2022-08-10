from color_refinement import *
from libraries.graph_io import *
import time
import sys

arguments = sys.argv[1:]
if len(arguments) == 0:
    file_name = 'colorref_smallexample_4_16.grl'
else:
    file_name = arguments[0]
start_time = time.time()
with open('../partition_refinement/test_files/' + file_name) as f:
    graphs = load_graph(f, read_list=True)

color_refinement(graphs[0])
print("--- %s seconds ---" % (time.time() - start_time))
