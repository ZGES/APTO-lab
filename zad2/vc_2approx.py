import dimacs as dim
import copy


def coverage_2approx(name):
    # load graph
    path = 'graph\\' + name
    graph = dim.loadGraph(path)
    solution_path = path + '.sol'

    # find coverage
    graph_list = dim.edgeList(graph)
    vertices = len(graph)

    graph_copy = copy.deepcopy(graph)
    solution = find_coverage(graph_copy, vertices, graph_list)
    dim.saveSolution(solution_path, solution)
    print('Solution for: ' + name + ' saved')


def find_coverage(graph, vertices, valid_graph):
    graph_list = dim.edgeList(graph)
    solution = set()

    while len(solution) < vertices - 1 and graph_list:
        u, v = graph_list.pop()
        graph_list = remove_edges(graph, u, v)
        solution.add(u)
        solution.add(v)
        if solution is not None and dim.isVC(valid_graph, solution):
            return solution


def remove_edges(graph, u, v):
    for neigh_u in graph[u].copy():
        graph[u].remove(neigh_u)
        graph[neigh_u].remove(u)

    for neigh_v in graph[v].copy():
        graph[v]. remove(neigh_v)
        graph[neigh_v].remove(v)

    return dim.edgeList(graph)
