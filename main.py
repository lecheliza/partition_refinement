from color_refinement import *
from libraries import graph
from libraries.graph_io import *

sample_graph = graph.Graph(False, 4)
for i in range(1, 4):
    u = sample_graph.vertices[i - 1]
    v = sample_graph.vertices[i]
    edge = graph.Edge(u, v)
    sample_graph += edge
    i += 1
print(color_refinement(sample_graph))

# with open('') as f:
#     G = load_graph(f)
#
# with open('', 'w') as f:
#     save_graph(sample_graph, f)
