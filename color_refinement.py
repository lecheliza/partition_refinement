from libraries import graph
from libraries import graph_io
import itertools


# this function determines if two vertices have similarly colored neighbourhoods
def have_same_neighbours(u: "graph.Vertex", v: "graph.Vertex"):
    # obviously, they cannot have the same neighbours if they have different amount of them
    if u.degree != v.degree:
        return False
    for u_n in u.neighbours:
        for v_n in v.neighbours:
            # if neighbour color in u is the same in the neighbour color in v and they are not the same vertex
            if u_n.color == v_n.color and u_n != v_n:
                print(f'color {u_n.color} and {v_n.color} for vertices {u_n.label} and {v_n.label}')
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
    # assign first colors to the vertices based on their degrees
    for vertex in g.vertices:
        vertex.color = vertex.degree
        if vertex.color not in colors:
            colors.append(vertex.color)
    for color in colors:
        colors_with_neighbourhoods[color] = []

    while True:
        colors_before = colors.copy()
        # compare all vertices with each other
        for u, v in itertools.combinations(g.vertices, 2):
            # case 1: they have the same color but different neighbourhoods -> they need to be colored differently
            if u.color == v.color and not have_same_neighbours(u, v):
                # keep the old color in a separate field
                u.previous_color = u.color
                # make sure that colors are sorted in ascending order
                colors.sort()
                # take the last color and increase it to the next one
                brand_new_color = colors[-1] + 1
                # assign new color to the vertex
                u.color = brand_new_color
                # add color to the list of used colors
                colors.append(brand_new_color)
                # to make sure that every color has own unique neighbourhood, I'd like to store them in a map, but
                # I'm not sure if it is a good way
                # because - what if now two colors have different neighbourhoods?
                # it is possible in the early iteration step...
                colors_with_neighbourhoods[brand_new_color] = map_neighbours_to_colors(u)
            # otherwise, if colors aren't the same but their neighbours are the same, they should have the same color
            elif u.color != v.color and have_same_neighbours(u, v):
                u.previous_color = u.color
                u.color = v.color
        colors_after = colors.copy()
        if colors_after == colors_before:
            break
    return graph
