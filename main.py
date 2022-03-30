from color_refinement import *
from fast_partition_refinement import fast_partition_refinement
from libraries.graph import *
from libraries.graph_io import *
import time

start_time = time.time()
with open('../partition_refinement/test_files/colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)

color_refinement(graphs[0])
print("--- %s seconds ---" % (time.time() - start_time))
