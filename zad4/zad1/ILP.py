from pulp import *

"""
Solve ILP:
-> minimize x + y
-> y >= x - 1
-> y >= -4x + 4
-> y <= -0.5x + 3
"""

# create model
model = LpProblem("IntegerLP", LpMinimize)
# define variables
x = LpVariable("x", cat="Integer")
y = LpVariable("y", cat="Integer")

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
    print(var.name, " = ", int(var.varValue))

print("OBJECTIVE: ", value(model.objective))

