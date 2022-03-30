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


def append_colored_neighbours(object_list, result_list):
    for n in object_list:  # here I want to get colors of the neighbours
        auxiliary_list = (v.colornum for v in n)  # fill the list with neighbours colors
        result_list.append(sorted(auxiliary_list))
    return


def initialize_graph(graph_vertices, queue, map_of_colors):
    for vertex in graph_vertices:
        new_color = vertex.degree
        vertex.colornum = new_color
        if new_color not in queue:
            queue.append(new_color)
        if new_color not in map_of_colors:
            map_of_colors[new_color] = [vertex]
        else:
            map_of_colors[new_color].append(vertex)
    return


def fast_partition_refinement(g_list):
    input_graph = Graph(False)
    for g in g_list:
        input_graph = input_graph + g
    w = deque()
    colors_with_vertices, colors_to_add, c_t_d = dict(), dict(), []
    initialize_graph(input_graph.vertices, w, colors_with_vertices)
    while w:
        colors_to_add.clear(), c_t_d.clear()
        higher_color = max(w) + 1
        a = w.popleft()
        for color in colors_with_vertices.keys():
            occurrences_to_vertices = map_occurrences_with_vertices(colors_with_vertices[color], a)
            if len(occurrences_to_vertices) == 1:
                continue
            needed_index = max(occurrences_to_vertices, key=lambda x: len(occurrences_to_vertices[x]))
            occurrences_to_vertices.pop(needed_index)
            for vertices_for_new_color in occurrences_to_vertices.values():
                colors_to_add[higher_color] = []
                for vertex in vertices_for_new_color:
                    colors_with_vertices[vertex.colornum].remove(vertex)
                    vertex.colornum = higher_color
                    colors_to_add[higher_color].append(vertex)
                w.append(higher_color)
                higher_color += 1
        for k in c_t_d:
            colors_with_vertices.pop(k)
        colors_with_vertices.update(colors_to_add)
    with open('../partition_refinement/test_files/done1.dot', 'w') as f:
        write_dot(input_graph, f)
    return


with open('../partition_refinement/test_files/colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)

start_time = time.time()
fast_partition_refinement(graphs[0])
print("--- %s seconds ---" % (time.time() - start_time))
