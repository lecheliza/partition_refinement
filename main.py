from color_refinement import *
from fast_partition_refinement import fast_partition_refinement
from libraries.graph import *
from libraries.graph_io import *
import time

start_time = time.time()
with open('../partition_refinement/test_files/SignOffColRefBackup5.grl') as f:
    graphs = load_graph(f, read_list=True)

huge_graph = graph.Graph(False)
for g in graphs[0]:
    huge_graph = huge_graph + g
# n = color_refinement(huge_graph)
fast_partition_refinement(huge_graph)
print("--- %s seconds ---" % (time.time() - start_time))
