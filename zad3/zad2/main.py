import zad2.vertex_cover as vc
import zad2.dimacs as dim

graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    "s25",
    "s50",
    "m20",
    "p20",
    "p35",
    "p60",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01"
]

for name in graph_names:
    path = 'graph\\' + name
    solution_filename = 'graph\\' + name + '.sol'

    graph = dim.loadGraph(path)
    graph_list = dim.edgeList(graph)
    solution = []

    for k in range(1, len(graph)):
        solution = vc.solve_vc(graph, k)
        if solution is not None and dim.isVC(graph_list, solution):
            dim.saveSolution(solution_filename, solution)
            print('Found solution for graph ' + name)
            break
