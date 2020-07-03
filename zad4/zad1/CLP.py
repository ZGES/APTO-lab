from pulp import *

"""
Solve Continuous LP:
-> minimize x + y
-> y >= x - 1
-> y >= -4x + 4
-> y <= -0.5x + 3
"""

# create model
model = LpProblem("ContinuousLP", LpMinimize)
# define variables
x = LpVariable("x", cat="Continuous")
y = LpVariable("y", cat="Continuous")

# add objective function
model += x + y

# add limits
model += y >= x - 1
model += y >= -4 * x + 4
model += y <= -0.5 * x + 3

print(model)

# solve model using CBC
model.solve()

print("STATUS: ", LpStatus[model.status])

print("VARIABLES:")
for var in model.variables():
    print(var.name, " = ", var.varValue)

print("OBJECTIVE: ", value(model.objective))

