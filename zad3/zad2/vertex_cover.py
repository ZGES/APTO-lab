import pycosat
import zad2.dimacs as dim


def solve_vc(graph, k):
    cnf = []
    n = len(graph)

    valuate(n, cnf)
    edges_cover(graph, cnf)
    set_y_0s(n, cnf)
    implication_to_cnf(n, cnf)
    cnf.append([-index(n - 1, k + 1, n)])

    result = pycosat.solve(cnf)

    if result == "UNSAT":
        return None
    else:
        vertices = result[:n]
        result = [x for x in vertices if x > 0]
        return result


def valuate(n, cnf):
    cnf.extend([[v, -v] for v in range(1, n)])


def edges_cover(graph, cnf):
    edges = dim.edgeList(graph)
    clauses = [[u, v] for u, v in edges]
    cnf.extend(clauses)


def set_y_0s(n, cnf):
    clauses_true = [[index(i, 0, n)] for i in range(0, n)]
    clauses_false = [[index(0, j, n)] for j in range(1, n)]
    cnf.extend(clauses_true)
    cnf.extend(clauses_false)


def implication_to_cnf(n, cnf):
    for i in range(1, n):
        for j in range(1, n):
            cnf.extend([[-index(i-1, j, n), index(i, j, n)], [-index(i-1, j-1, n), -i, index(i, j, n)]])


def index(i, j, n):
    return int(n - 1 + (i + j) * (i + j + 1) / 2 + i) + 1
