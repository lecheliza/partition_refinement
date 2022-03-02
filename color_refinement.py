from libraries import graph
from libraries import graph_io
import itertools


# some way to get colored neighbourhood

def have_same_neighbours(u: "graph.Vertex", v: "graph.Vertex"):
    if u.degree != v.degree:
        return False
    for u_n in u.neighbours:
        for v_n in v.neighbours:
            if u_n.color == v_n.color and u_n != v_n:
                return True
    return False


def map_neighbours_to_colors(u: "graph.Vertex"):
    colored = []
    for neighbour in u.neighbours:
        colored.append(neighbour.color)
    return colored


def color_refinement(g: "graph.Graph"):
    # here I can keep track of colors that have been used
    colors = []
    # and here I want to keep track of associating colors with neighbourhoods
    colors_with_neighbourhoods = {}
    for vertex in g.vertices:
        vertex.color = vertex.degree
        if vertex.color not in colors:
            colors.append(vertex.color)
    for color in colors:
        colors_with_neighbourhoods[color] = []

    i = 0
    while i < 1:
        i += 1
        for u, v in itertools.combinations(g.vertices, 2):
            if u.color == v.color and not have_same_neighbours(u, v):
                u.previous_color = u.color
                colors.sort()
                brand_new_color = colors[-1] + 1
                u.color = brand_new_color
                colors.append(brand_new_color)
                # here place new neighbourhood
                colors_with_neighbourhoods[brand_new_color] = map_neighbours_to_colors(u)
            elif u.color == v.color and have_same_neighbours(u, v):
                u.color = v.color
        print(colors)
    return
