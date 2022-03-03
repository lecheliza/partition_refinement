from libraries import graph
import itertools


# this function determines if two vertices have similarly colored neighbourhoods
def have_same_neighbours(u: "graph.Vertex", v: "graph.Vertex"):
    # obviously, they cannot have the same neighbours if they have different amount of them
    if u.degree != v.degree:
        return False
    # create two lists for storing the colors in the neighbourhoods of two vertices
    u_colored_neighbours = []
    v_colored_neighbours = []
    # add colors to the lists
    for u_n in u.neighbours:
        u_colored_neighbours.append(u_n.color)
    for v_n in v.neighbours:
        v_colored_neighbours.append(v_n.color)
    # to make sure that the result of this function will be correct, I sort the lists
    u_colored_neighbours.sort()
    v_colored_neighbours.sort()
    # compare the lists
    if u_colored_neighbours != v_colored_neighbours:
        return False
    return True


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
    while True:
        colors_before = colors.copy()
        # compare all vertices with each other
        for u, v in itertools.combinations(g.vertices, 2):
            # case 1: they have the same color but different neighbourhoods -> they need to be colored differently
            if u.color == v.color and not have_same_neighbours(u, v):
                # make sure that colors are sorted in ascending order
                colors.sort()
                # take the last color and increase it to the next one
                brand_new_color = colors[-1] + 1
                # assign new color to the vertex
                u.color = brand_new_color
                # add color to the list of used colors
                colors.append(brand_new_color)
            # otherwise, if colors aren't the same but their neighbours are the same, they should have the same color
            elif u.color != v.color and have_same_neighbours(u, v):
                v.previous_color = v.color
                v.color = u.color
        colors_after = colors.copy()
        # for v in g.vertices:
        #     print(f'vertex {v.label} has color {v.color}')
        if colors_after == colors_before:
            for color in colors:
                colors_with_neighbourhoods[color] = []
            for vertex in g.vertices:
                for neighbour in vertex.neighbours:
                    if len(colors_with_neighbourhoods[vertex.color]) < vertex.degree:
                        colors_with_neighbourhoods[vertex.color].append(neighbour.color)
                        colors_with_neighbourhoods[vertex.color].sort()
            break
    return colors_with_neighbourhoods
