from libraries import graph
from libraries import graph_io


# some way to get colored neighbourhood

def color_refinement(g: "graph.Graph"):
    for vertex in g.vertices:
        vertex.color = vertex.degree
    i = 0
    for vertex in g.vertices:
        vertex.previous_color = vertex.color
        vertex.color = i
        while True:
            if vertex.color == vertex.color:
                break

    # the plan is to:
    # iterate through neighbourhood and see if the vertices with the same colour have same neighbourhoods
    # if they don't, then change the colour to the next one that is suitable
    # what to do with the colouring? how to distinct them? dict?
    return
