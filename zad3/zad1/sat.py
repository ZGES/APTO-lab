import random
import pycosat


def generate_result(k, n, T):
    sign = [-1, 1]
    var_list = range(1, n + 1)
    stats = []

    for a in [x * 0.1 for x in range(10, 100)]:
        clause_number = int(a * n)
        percent = get_satisfiability_percent(k, var_list, sign, clause_number, T)
        stats.append((a, percent))
    return stats


def get_satisfiability_percent(k, var_list, sign, clause_number, T):
    counter = 0
    for i in range(0, T):
        cnf = generate_cnf(k, var_list, sign, clause_number)
        if pycosat.solve(cnf) != 'UNSAT':
            counter += 1
    return counter/T


def generate_cnf(k, var_list, sign, clause_number):
    cnf = []
    for i in range(0, clause_number):
        clause = generate_clause(k, var_list, sign)
        cnf.append(clause)
    return cnf


def generate_clause(k, var_list, sign):
    clause = []
    for i in range(0, k):
        x = random.choice(var_list) * random.choice(sign)
        clause.append(x)
    return clause
