from zad2 import dimacs as dim
from pulp import *


def solveWeightedVC(graph, level):
    vertices = len(graph)
    graph_list = dim.edgeList(graph)

    weights = getWeights(getDegrees(graph), level)

    model = LpProblem("Weighted_Vertex_Cover", LpMinimize)
    variables = []

    for i in range(1, vertices):
        variables.append(LpVariable(str(i), cat="Binary") * weights[i])

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


def getDegrees(graph):
    degrees = [0]

    for v in range(1, len(graph)):
        degree = len(graph[v])
        degrees.append(degree)

    return degrees


def getWeights(degrees, level):
    for i in range(1, len(degrees)):
        degrees[i] = degrees[i] ** level

    return degrees

