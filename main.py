from color_refinement import *
from libraries import graph
from libraries.graph_io import *


def compare_graphs(list_of_graphs):
    i = 0
    for one_graph in list_of_graphs:
        one_graph.colors = color_refinement(one_graph)
        one_graph.label = i
        i += 1
    print('Sets of possible isomorphic graphs:')
    for one_graph, second_graph in itertools.combinations(list_of_graphs, 2):
        if one_graph.colors == second_graph.colors:
            print(
                f"[{one_graph.label}, "
                f"{second_graph.label}]"
                f" {'discrete' if len(one_graph.colors.keys()) == len(one_graph.vertices) else ''}")


# sample_graph = graph.Graph(False, 7)
# for i in range(1, 7):
#     u = sample_graph.vertices[i - 1]
#     v = sample_graph.vertices[i]
#     edge = graph.Edge(u, v)
#     sample_graph += edge
#     i += 1
# print(color_refinement(sample_graph))

with open('test_files/colorref_smallexample_4_7.grl') as f:
    g0 = load_graph(f)
    g1 = load_graph(f)
    g2 = load_graph(f)
    g3 = load_graph(f)

list_graphs = [g0, g1, g2, g3]
# print(compare_graphs(list_graphs))

print(color_refinement(g1))
print(color_refinement(g3))

# with open('test_files/done_example.dot', 'w') as f:
#     save_graph(G, f)
