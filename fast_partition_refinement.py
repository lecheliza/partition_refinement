from libraries.graph import *
from libraries.graph_io import load_graph


def add_to_adequate_color(m: "dict", s1: "set", s2: "set"):
    for color in m.keys():
        s1.add(tuple(m[color]))
        s2.add(color)


def fast_partition_refinement(input_graph: "Graph"):
    p, w = set(), set()
    vertex_to_color = {}
    for v in input_graph.vertices:
        v.colornum = v.degree
        if v.colornum not in vertex_to_color.keys():
            vertex_to_color[v.colornum] = [v]
        else:
            vertex_to_color[v.colornum].append(v)
    add_to_adequate_color(vertex_to_color, p, w)
    highest_color = max(w)
    print(highest_color)
    while w:
        a = w.pop()
        vertices_with_given_color = [v for v in input_graph.vertices if v.colornum == a]

        # print([v.colornum for v in [ver for ver in x]])
        # print([v.neighbours for v in input_graph.vertices if v.colornum == a])
        for vertex in vertices_with_given_color:
            highest_color += 1
            vertex.colornum = highest_color
        # w.add(highest_color)
    return


with open('../partition_refinement/test_files/colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)

fast_partition_refinement(graphs[0][0])
