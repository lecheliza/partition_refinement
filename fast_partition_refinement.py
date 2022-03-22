import time
from collections import deque
from libraries.graph_io import *


def map_occurrences_with_vertices(vertices_list, color):
    dictionary = {}
    for vertex in vertices_list:
        number_of_occurrences = len([n for n in vertex.neighbours if n.colornum == color])
        if number_of_occurrences in dictionary:
            dictionary[number_of_occurrences].append(vertex)
        else:
            dictionary[number_of_occurrences] = [vertex]
    return dictionary


def fast_partition_refinement(input_graph: "Graph"):
    w, colors = deque(), []
    for v in input_graph.vertices:
        v.colornum = v.degree
        if v.colornum not in colors:
            colors.append(v.colornum)
    colors.sort()
    for color in colors:
        w.append(color)
    while w:
        higher_color = max(w) + 1
        a = w.popleft()
        c = 0
        while c < len(colors):
            color = colors[c]
            # vertices_with_color = []
            # for vertex in input_graph.vertices:
            #     if vertex.colornum == color:
            #         vertices_with_color.append(vertex)
            vertices_with_color = [v for v in input_graph.vertices if v.colornum == color]
            occurrences_to_vertices = map_occurrences_with_vertices(vertices_with_color, a)
            if occurrences_to_vertices:
                needed_index = max(occurrences_to_vertices, key=lambda x: len(occurrences_to_vertices[x]))
                occurrences_to_vertices.pop(needed_index)
                for vertices_for_new_color in occurrences_to_vertices.values():
                    for vertex in vertices_for_new_color:
                        vertex.colornum = higher_color
                    w.append(higher_color)
                    colors.append(higher_color)
                    higher_color += 1
            c += 1
    with open('../partition_refinement/test_files/done1.dot', 'w') as f:
        write_dot(input_graph, f)
    return


with open('../partition_refinement/test_files/SignOffColRefBackup5.grl') as f:
    graphs = load_graph(f, read_list=True)

start_time = time.time()
huge_graph = Graph(False)
# for g in graphs[0]:
#     huge_graph = huge_graph + g
fast_partition_refinement(graphs[0][0] + graphs[0][2])
print("--- %s seconds ---" % (time.time() - start_time))
