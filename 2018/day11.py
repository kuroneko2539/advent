import numpy as np

serialNo = 6878
grid = np.zeros((300,300))

def calcValue(i,j):
    i = i + 1
    j = j + 1

    rack = i + 10
    val = rack * j
    val += serialNo
    val *= rack
    val = str(val)
    if len(val) < 3:
        val = 0
    else:
        val = int(val[-3])
    val = val -5

    return val

for i in range(300):
    for j in range(300):
        grid[i,j] = calcValue(i,j)

bestVal = -100
bestI, bestJ = 0,0
for i in range(298):
    for j in range(298):
        sumVal = np.sum(grid[i:i+3,j:j+3])
        if sumVal > bestVal:
            bestVal = sumVal
            bestI = i + 1
            bestJ = j + 1

print("{},{}: {}".format(bestI,bestJ, bestVal))

bestVal = -100
bestI, bestJ, bestSize = 0,0,0
for size in range(1,301):
    for i in range(301-size):
        for j in range(301-size):
            sumVal = np.sum(grid[i:i+size,j:j+size])
            if sumVal > bestVal:
                bestVal = sumVal
                bestI = i + 1
                bestJ = j + 1
                bestSize = size
    print(size)
    print("{},{},{}: {}".format(bestI,bestJ,bestSize, bestVal))

print("{},{},{}: {}".format(bestI,bestJ,bestSize, bestVal))