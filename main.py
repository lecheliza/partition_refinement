from color_refinement import *
from libraries import graph
from libraries.graph_io import *


# def create_graph_with_path(number_of_vertices):
#     graph_to_be_returned = Graph(False, number_of_vertices)
#     for i in range(1, number_of_vertices):
#         u = graph_to_be_returned.vertices[i - 1]
#         v = graph_to_be_returned.vertices[i]
#         edge = Edge(u, v)
#         graph_to_be_returned += edge
#         i += 1
#     return graph_to_be_returned
#
#
# def create_graph_with_cycle(number_of_vertices):
#     graph_to_be_returned = create_graph_with_path(number_of_vertices)
#     first_vertex = graph_to_be_returned.vertices[0]
#     last_vertex = graph_to_be_returned.vertices[number_of_vertices - 1]
#     edge = Edge(first_vertex, last_vertex)
#     graph_to_be_returned += edge
#     return graph_to_be_returned
#
#
# def create_complete_graph(number_of_vertices):
#     complete_graph = create_graph_with_cycle(number_of_vertices)
#     for v in range(len(complete_graph.vertices)):
#         for v2 in range(v, len(complete_graph.vertices)):
#             u = complete_graph.vertices[v]
#             u1 = complete_graph.vertices[v2]
#             if not complete_graph.find_edge(u, u1) and u != u1:
#                 complete_graph.add_edge(Edge(u, u1))
#     return complete_graph


sample_graph = graph.Graph(False, 7)
for i in range(1, 7):
    u = sample_graph.vertices[i - 1]
    v = sample_graph.vertices[i]
    edge = graph.Edge(u, v)
    sample_graph += edge
    i += 1
print(color_refinement(sample_graph))

# with open('test_files/colorref_smallexample_4_7.grl') as f:
#     G = load_graph(f)

# print(color_refinement(G))
# with open('test_files/done_example.dot', 'w') as f:
#     save_graph(G, f)
