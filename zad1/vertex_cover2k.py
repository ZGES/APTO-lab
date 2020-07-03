import dimacs as dim
from copy import copy


def check_coverage(name):
    path = 'graph\\' + name
    solution_filename = 'graph\\' + name + '.sol'
    graph = dim.loadGraph(path)
    graph_list = dim.edgeList(graph)
    vertices = len(graph)
    solution = set()
    size = 0

    for k in range(1, vertices):
        if not graph[k]:
            solution.add(k)
            size += 1

    solution_copy = copy(solution)
    for k in range(size, vertices):
        solution = find_coverage(graph_list, solution_copy, k)
        if solution is not None and dim.isVC(graph_list, solution):
            dim.saveSolution(solution_filename, solution)
            break


def find_coverage(graph, solution, size):
    if not graph:
        return solution

    if size == 0:
        return None

    u, v = graph.pop()

    graph_u = [(a, b) for (a, b) in graph
               if not (a == u or b == u)]

    solution_copy = copy(solution)
    solution_copy.add(u)

    solution_1 = find_coverage(graph_u, solution_copy, size - 1)
    if solution_1:
        return solution_1

    graph_v = [(a, b) for (a, b) in graph
               if not (a == v or b == v)]

    solution.add(v)

    solution_2 = find_coverage(graph_v, solution, size - 1)
    if solution_2:
        return solution_2


graph_name = input()
check_coverage(graph_name)