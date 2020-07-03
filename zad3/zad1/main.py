import zad1.sat as sat

stats = sat.generate_result(3, 50, 100)

f = open("results.txt", 'w+')
for i in range(len(stats)):
    a, percent = stats[i]
    f.write(str(a) + " " + str(percent) + "\n")
f.close()
