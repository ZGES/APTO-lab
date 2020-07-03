from time import time

from zad2 import dimacs as dim
from zad2 import vertexCover as vc
from zad2 import weightedVC as wvc
from zad2 import approxVC as avc

graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    "e150",
    "s25",
    "s50",
    "s500",
    "b20",
    "b30",
    "b100",
    "k330_a",
    "k330_b",
    "k330_c",
    "m20",
    "m30",
    "m40",
    "m50",
    "m100",
    "p20",
    "p35",
    "p60",
    "p150",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    "r100_01",
    "r100_005"]

for name in graph_names:
    path = '..\\graph\\' + name
    sol_name = path + '.sol'
    w_sol_name = path + 'W.sol'
    a_sol_name = path + 'A.sol'

    graph = dim.loadGraph(path)
    graph_list = dim.edgeList(graph)

    timeExact = time()
    solution = vc.solveVC(graph)
    timeExact = round(time() - timeExact, 5)

    timeWeight = time()
    solutionW = wvc.solveWeightedVC(graph, 1.0)
    timeWeight = round(time() - timeWeight, 5)

    timeApprox = time()
    solutionA = avc.approxSolveVC(graph)
    timeApprox = round(time() - timeApprox, 5)

    if solution is not None and dim.isVC(graph_list, solution):
        #dim.saveSolution(sol_name, solution)
        print("Solved ", name, "using ", len(solution), " vertices in time: ", timeExact)
    if solutionW is not None and dim.isVC(graph_list, solutionW):
        #dim.saveSolution(w_sol_name, solutionW)
        print("Solved with weight ", name, "using ", len(solutionW), " vertices in time: ", timeWeight)
    if solutionA is not None and dim.isVC(graph_list, solutionA):
        #dim.saveSolution(a_sol_name, solutionA)
        print("Solved with approximation ", name, "using ", len(solutionA), " vertices in time: ", timeApprox)
    print("\n")
