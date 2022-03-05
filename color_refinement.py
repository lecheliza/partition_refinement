from libraries import graph
import itertools
from libraries import graph_io


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
        u_colored_neighbours.append(u_n.colornum)
    for v_n in v.neighbours:
        v_colored_neighbours.append(v_n.colornum)
    # to make sure that the result of this function will be correct, I sort the lists
    u_colored_neighbours.sort()
    v_colored_neighbours.sort()
    # compare the lists
    if u_colored_neighbours != v_colored_neighbours:
        return False
    return True


def list_to_dict(colors_list):
    dict_to_be_returned = {}
    for c in colors_list:
        d = tuple(c)
        if d in dict_to_be_returned.keys():
            dict_to_be_returned[d] += 1
        else:
            dict_to_be_returned[d] = 1
    return dict_to_be_returned


def color_refinement(g: "graph.Graph"):
    # here I can keep track of colors that have been used
    colors = []
    # and here I want to keep track of associating colors with neighbourhoods
    colors_with_neighbourhoods = {}
    # assign first colors to the vertices based on their degrees
    for vertex in g.vertices:
        vertex.colornum = vertex.degree
        if vertex.colornum not in colors:
            colors.append(vertex.colornum)
    while True:
        colors_before = colors.copy()
        for u in g.vertices:
            list1 = []
            list_vertices_obj = []
            vertices_that_are_similar = []
            for v_c in g.vertices:
                if v_c.colornum == u.colornum:
                    vertices_that_are_similar.append(v_c)
            for color_v in vertices_that_are_similar:
                list2 = []
                list_vertices_obj.append(color_v)
                for neighbours in color_v.neighbours:
                    list2.append(neighbours.colornum)
                list1.append(list2)
            map1 = list_to_dict(list1)
            print(list_vertices_obj)
            minimal_color_occurences = min(map1, key=map1.get)
            minimal_color_occurences = list(minimal_color_occurences)
            print(minimal_color_occurences)
            vertices_to_be_changed = []
            for index in range(0, len(list1)):
                if list1[index] == minimal_color_occurences:
                    new_color = max(colors) + 1
                    list_vertices_obj[index].colornum = new_color
                    colors.append(new_color)
                    print(colors)
            print(vertices_to_be_changed)
        # compare all vertices with each other
        for u, v in itertools.combinations(g.vertices, 2):
            # case 1: they have the same color but different neighbourhoods -> they need to be colored differently
            if u.colornum == v.colornum and not have_same_neighbours(u, v):
                print(f'vertex {u.label} and vertex {v.label}')
                # find the list of vertices that are in the same situation --> colors etc

                # lista list sąsiadów
                # make sure that colors are sorted in ascending order
                colors.sort()
                # take the last color and increase it to the next one
                brand_new_color = colors[-1] + 1
                # assign new color to the vertex
                u.colornum = brand_new_color
                # add color to the list of used colors
                colors.append(brand_new_color)
            # otherwise, if colors aren't the same but their neighbours are the same, they should have the same color
            elif u.colornum != v.colornum and have_same_neighbours(u, v):
                v.colornum = u.colornum
        colors_after = colors.copy()
        if colors_after == colors_before:
            for index in colors:
                colors_with_neighbourhoods[index] = []
            for vertex in g.vertices:
                for neighbour in vertex.neighbours:
                    if len(colors_with_neighbourhoods[vertex.colornum]) < vertex.degree:
                        colors_with_neighbourhoods[vertex.colornum].append(neighbour.colornum)
                        colors_with_neighbourhoods[vertex.colornum].sort()
            with open('test_files/done.dot', 'w') as f:
                graph_io.write_dot(g, f)
            break
    return colors_with_neighbourhoods

# def color_refinement(g: "graph.Graph"):
#     vertex_with_colors = {}
