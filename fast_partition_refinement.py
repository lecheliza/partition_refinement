from collections import deque
from libraries import graph_io
from libraries.graph import *
from libraries.graph_io import load_graph


def add_to_adequate_color(m: "list", s2: "deque"):
    m.sort()
    for color in m:
        s2.append(color)


def fast_partition_refinement(input_graph: "Graph"):
    w = deque()
    colors = []
    for v in input_graph.vertices:
        v.colornum = v.degree
        if v.colornum not in colors:
            colors.append(v.colornum)
    add_to_adequate_color(colors, w)
    while w:
        next_color = max(w) + 1
        a = w.popleft()
        for color in range(1, next_color):
            occurrences_to_vertices = {}
            vertices_with_examined_color = [v for v in input_graph.vertices if v.colornum == color]
            for vertex in vertices_with_examined_color:
                index = 0
                for n in vertex.neighbours:
                    if n.colornum == a:
                        index += 1
                if index not in occurrences_to_vertices.keys():
                    occurrences_to_vertices[index] = [vertex]
                else:
                    occurrences_to_vertices[index].append(vertex)
            index_of_biggest_occurences = 0
            number_of_vertices_in_this_index = 0
            for item in occurrences_to_vertices.items():
                num_ver = len(item[1])
                if number_of_vertices_in_this_index < num_ver:
                    number_of_vertices_in_this_index = num_ver
                    index_of_biggest_occurences = item[0]
            occurrences_to_vertices.pop(index_of_biggest_occurences)
            for ncc in occurrences_to_vertices.values():
                for v in ncc:
                    v.colornum = next_color
                w.append(next_color)
                next_color += 1
    with open('../partition_refinement/test_files/done1.dot', 'w') as f:
        graph_io.write_dot(input_graph, f)
    return


with open('../partition_refinement/test_files/colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)

fast_partition_refinement(graphs[0][0])
