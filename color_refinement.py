import itertools
from collections import defaultdict

from libraries import graph, graph_io


def list_to_dict(colors_list):
    dict_to_be_returned = defaultdict(int)
    for c in colors_list: dict_to_be_returned[tuple(c)] += 1
    return dict_to_be_returned


def longest(input_list):
    largest_number = max(len(element) for element in input_list)
    longest_list = (x for x in input_list if len(x) == largest_number)
    return longest_list


def initialize_colors(g, colors):
    for vertex in g.vertices:  # assign first colors to the vertices based on their degrees
        vertex.colornum = vertex.degree
        if vertex.colornum not in colors:
            colors.append(vertex.colornum)


def color_refinement(g: "graph.Graph", input_length: int):
    colors = []  # here I can keep track of colors that have been used
    initialize_colors(g, colors)
    current_color_vertices, current_color_neighbourhoods_as_objects, current_color_neighbourhoods_as_colors = [], [], []
    while True:
        colors_before = tuple(colors)
        for current_color in colors:
            current_color_vertices.clear()
            current_color_neighbourhoods_as_objects.clear()
            current_color_neighbourhoods_as_colors.clear()
            for v in g.vertices:  # iterate through the whole graph
                if v.colornum == current_color:  # if current vertex has the color I want
                    current_color_vertices.append(v)  # I add it to the list with all vertices with this color
                    current_color_neighbourhoods_as_objects.append(v.neighbours)  # and I add its neighbours
            for n in current_color_neighbourhoods_as_objects:  # here I want to get colors of the neighbours
                auxiliary_list = (v.colornum for v in n)
                current_color_neighbourhoods_as_colors.append(sorted(auxiliary_list))
            color_to_occurrences = list_to_dict(current_color_neighbourhoods_as_colors)  # map in which i can
            # keep track of neighbours and how many times they occur for that color
            while len(color_to_occurrences) > 1:  # so I want to change colors of those which
                # occurs the lowest number of times
                neighbours_that_are_different = min(color_to_occurrences, key=color_to_occurrences.get)
                neighbours_that_are_different = list(neighbours_that_are_different)
                new_color = max(colors) + 1
                for z in range(len(current_color_neighbourhoods_as_colors)):
                    if current_color_neighbourhoods_as_colors[z] == neighbours_that_are_different:
                        current_color_vertices[z].colornum = new_color
                        if new_color not in colors:
                            colors.append(new_color)
                color_to_occurrences.pop(tuple(neighbours_that_are_different))
        colors_after = tuple(colors)
        if colors_before == colors_after:
            subgraphs = []
            start_index = 0
            label = 0
            for sg in range(1, len(g.vertices) + 1):
                if sg % input_length == 0:
                    new_graph = graph.Graph(g.directed, input_length)
                    new_graph.label = label
                    new_graph.colors = []
                    auxiliary_index = 0
                    for v in g.vertices[start_index:sg]:
                        new_graph.vertices.append(v)
                        new_graph.vertices[auxiliary_index].colornum = v.colornum
                        new_graph.colors.append(v.colornum)
                        auxiliary_index += 1
                    start_index = sg
                    new_graph.colors.sort()
                    subgraphs.append(new_graph)
                    label += 1
            for u, v in itertools.combinations(subgraphs, 2):
                if u.colors == v.colors:
                    print(
                        f"Potentially isomorphic graphs: {u.label}, {v.label} {'discrete' if len(u.colors) == len(u.vertices) else ''}")
            with open('../partition_refinement/test_files/done1.dot', 'w') as f:
                graph_io.write_dot(g, f)
            break
    return g
