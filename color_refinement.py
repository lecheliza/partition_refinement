from itertools import combinations
from collections import defaultdict
import numpy as np
from libraries import graph, graph_io


def list_to_dict(colors_list):
    dict_to_be_returned = defaultdict(int)
    for c in colors_list:
        dict_to_be_returned[tuple(c)] += 1  # fill it with the number of occurrences of such color in neighbourhood
    return dict_to_be_returned


def longest(input_list):
    largest_number = max(len(element) for element in input_list)  # find the largest element (returns its size)
    longest_list = (x for x in input_list if len(x) == largest_number)  # find the list with this size
    return longest_list


def initialize_colors(g, colors):
    for vertex in g.vertices:
        vertex.colornum = vertex.degree
        if vertex.colornum not in colors:
            colors.append(vertex.colornum)


def color_refinement(g: "graph.Graph", input_length: int):
    colors = []  # all the colors used in graphs
    initialize_colors(g, colors)
    # lists for: 1) vertices with examined color, 2) obj neighbourhoods of them, 3) like second but colors
    current_color_vertices, current_color_neighbourhoods_as_objects, current_color_neighbourhoods_as_colors = [], [], []
    while 1:
        colors_before = tuple(colors)
        for current_color in colors:  # iterate through all the colors that were defined
            current_color_vertices.clear()
            current_color_neighbourhoods_as_objects.clear()
            current_color_neighbourhoods_as_colors.clear()
            for v in g.vertices:
                if v.colornum == current_color:
                    current_color_vertices.append(v)  # add it to the list with all vertices with this color
                    current_color_neighbourhoods_as_objects.append(v.neighbours)  # and add its neighbours
            for n in current_color_neighbourhoods_as_objects:  # here I want to get colors of the neighbours
                auxiliary_list = (v.colornum for v in n)  # fill the list with neighbours colors
                current_color_neighbourhoods_as_colors.append(sorted(auxiliary_list))
            color_to_occurrences = list_to_dict(current_color_neighbourhoods_as_colors)
            while len(color_to_occurrences) > 1:  # so I want to change colors of those which
                # occurs the lowest number of times
                # get the tuple with smallest number of occurrences
                neighbours_that_are_different = list(min(color_to_occurrences, key=color_to_occurrences.get))
                new_color = max(colors) + 1
                for z in range(len(current_color_neighbourhoods_as_colors)):
                    # if the neighbour z is from the smallest tuple
                    if current_color_neighbourhoods_as_colors[z] == neighbours_that_are_different:
                        current_color_vertices[z].colornum = new_color  # change its color in object
                        if new_color not in colors:
                            colors.append(new_color)
                color_to_occurrences.pop(tuple(neighbours_that_are_different))  # this pair is not of this color anymore
        colors_after = tuple(colors)
        if colors_before == colors_after:  # if the colors changed, start comparing
            subgraphs, start_index, label = [], 0, 0
            for subgraph_index in range(1, len(g.vertices) + 1):
                if subgraph_index % input_length == 0:
                    new_graph = graph.Graph(g.directed, input_length)
                    new_graph.label = label  # I use it only for nice printing at the end
                    new_graph.colors = []  # list for storing all the colors that appeared in the graph
                    auxiliary_index = 0
                    for v in g.vertices[start_index:subgraph_index]:
                        new_graph.vertices.append(v)
                        new_graph.vertices[auxiliary_index].colornum = v.colornum
                        new_graph.colors.append(v.colornum)
                        auxiliary_index += 1
                    start_index = subgraph_index  # update starting index
                    new_graph.colors.sort()  # sorting helps in comparing
                    subgraphs.append(new_graph)
                    label += 1
            for u, v in combinations(subgraphs, 2):
                if u.colors == v.colors:
                    print(
                        f"Potentially isomorphic graphs: [{u.label}, {v.label}] "
                        f"{'discrete' if len(u.colors) == len(u.vertices) else ''}")
            # with open('../partition_refinement/test_files/done1.dot', 'w') as f:
            #     graph_io.write_dot(g, f)
            break
    return g
