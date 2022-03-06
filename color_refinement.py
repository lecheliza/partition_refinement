from libraries import graph, graph_io


def list_to_dict(colors_list):
    dict_to_be_returned = {}
    for c in colors_list:
        d = tuple(c)
        if d in dict_to_be_returned.keys():
            dict_to_be_returned[d] += 1
        else:
            dict_to_be_returned[d] = 1
    return dict_to_be_returned


def longest(input_list):
    largest_number = max(len(element) for element in input_list)
    longest_list = []
    for l in input_list:
        if len(l) == largest_number:
            longest_list = l
    return longest_list


def color_refinement(g: "graph.Graph"):
    # here I can keep track of colors that have been used
    colors = []
    # assign first colors to the vertices based on their degrees
    for vertex in g.vertices:
        vertex.colornum = vertex.degree
        if vertex.colornum not in colors:
            colors.append(vertex.colornum)
    color_index = 0
    while True:
        colors_before = colors.copy()
        # start with a color
        current_color = colors[color_index]
        # here I will store vertices that have the color I am currently examining
        current_color_vertices = []
        # here I will store neighbourhoods of the vertices I am currently examining
        current_color_neighbourhoods_as_objects = []
        # here I will store neighbourhoods AS COLORS
        current_color_neighbourhoods_as_colors = []
        # iterate through the whole graph
        for v in g.vertices:
            # if current vertex has the color I want
            if v.colornum == current_color:
                # I add it to the list with all vertices with this color
                current_color_vertices.append(v)
                # and I add its neighbours
                current_color_neighbourhoods_as_objects.append(v.neighbours)
        # here I want to get colors of the neighbours
        for n in current_color_neighbourhoods_as_objects:
            auxiliary_list = []
            for v in n:
                auxiliary_list.append(v.colornum)
                auxiliary_list.sort()
            current_color_neighbourhoods_as_colors.append(auxiliary_list)
        # map in which i can keep track of neighbours and how many times they occur for that color
        color_to_occurrences = list_to_dict(current_color_neighbourhoods_as_colors)
        # so I want to change colors of those which occurs the lowest number of times
        while len(color_to_occurrences) > 1:
            neighbours_that_are_different = min(color_to_occurrences, key=color_to_occurrences.get)
            neighbours_that_are_different = list(neighbours_that_are_different)
            new_color = max(colors) + 1
            for z in range(len(current_color_neighbourhoods_as_colors)):
                if current_color_neighbourhoods_as_colors[z] == neighbours_that_are_different:
                    current_color_vertices[z].colornum = new_color
                    if new_color not in colors:
                        colors.append(new_color)
            color_to_occurrences.pop(tuple(neighbours_that_are_different))
        color_index += 1
        colors_after = colors.copy()
        if colors_before == colors_after:
            with open('../partition_refinement/test_files/done1.dot', 'w') as f:
                graph_io.write_dot(g, f)
            break
    return g
