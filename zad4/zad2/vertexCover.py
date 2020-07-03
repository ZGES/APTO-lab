from zad2 import dimacs as dim
from pulp import *


def solveVC(graph):
    vertices = len(graph)
    graph_list = dim.edgeList(graph)

    model = LpProblem("Vertex_Cover", LpMinimize)
    variables = []

    for i in range(1, vertices):
        variables.append(LpVariable(str(i), cat="Binary"))

    model += sum(variables)

    for edge in graph_list:
        u, v = edge
        model += variables[u-1] + variables[v-1] >= 1

    model.solve()

    if LpStatus[model.status] == "Optimal":
        result = set()
        for var in model.variables():
            if var.varValue > 0:
                result.add(int(var.name))
        return result
    else:
        return None
