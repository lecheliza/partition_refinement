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

with open('../partition_refinement/test_files/colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)

huge_graph = graph.Graph(False)
for g in graphs[0]:
    huge_graph = huge_graph + g

n = color_refinement(huge_graph)

# print(compare_graphs(list_graphs))





# colors1 = {}
# colors2 = {}
# print(x.keys)
# for color in x.keys():
#     colors1[color] = 0
#     colors2[color] = 0
# for vertex in x.keys:
#     colors1[vertex] += 1
# for vertex in vertices_1:
#     colors2[vertex] += 1

# with open('test_files/done_example.dot', 'w') as f:
#     save_graph(G, f)

# with open('test_files/done_example.dot', 'w') as f:
#     write_dot(graphs[0][1], f)