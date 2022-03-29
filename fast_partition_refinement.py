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
    w, colors = deque(), set()
    colors_with_vertices = dict()
    for vertex in input_graph.vertices:
        new_color = vertex.degree
        vertex.colornum = new_color
        if new_color not in w:
            w.append(new_color)
        colors.add(new_color)
        if vertex.colornum not in colors_with_vertices:
            colors_with_vertices[new_color] = [vertex]
        else:
            colors_with_vertices[new_color].append(vertex)
    colors_to_add = set()
    while w:
        colors_to_add.clear()
        higher_color = max(w) + 1
        a = w.popleft()
        for color in colors:
            occurrences_to_vertices = map_occurrences_with_vertices(colors_with_vertices[color], a)
            if occurrences_to_vertices:
                needed_index = max(occurrences_to_vertices, key=lambda x: len(occurrences_to_vertices[x]))
                occurrences_to_vertices.pop(needed_index)
                for vertices_for_new_color in occurrences_to_vertices.values():
                    colors_with_vertices[higher_color] = []
                    for vertex in vertices_for_new_color:
                        colors_with_vertices[vertex.colornum].remove(vertex)
                        vertex.colornum = higher_color
                        colors_with_vertices[higher_color].append(vertex)
                    w.append(higher_color)
                    colors_to_add.add(higher_color)
                    higher_color += 1
        colors.update(colors_to_add)
    with open('../partition_refinement/test_files/done1.dot', 'w') as f:
        write_dot(input_graph, f)
    return


with open('../partition_refinement/test_files/SignOffColRefBackup5.grl') as f:
    graphs = load_graph(f, read_list=True)

start_time = time.time()
# huge_graph = Graph(False)
# for g in graphs[0]:
#     huge_graph = huge_graph + g
fast_partition_refinement(graphs[0][0] + graphs[0][1])
print("--- %s seconds ---" % (time.time() - start_time))
