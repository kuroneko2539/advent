import argparse, numpy as np
from collections import deque

numPlayers = 468
lastScoreMarble = 7101000

currentCircle = deque([0])
currentElf = 0
elfScores = list(np.zeros(numPlayers))

for i in range(1,lastScoreMarble + 1):
    if i % 23 == 0:
        elfScores[currentElf] += i
        elfScores[currentElf] += currentCircle[-7]
        currentCircle.rotate(6)
        del currentCircle[-1]
    else:
        placePos = 2 % len(currentCircle)
        currentCircle.insert(placePos, i)
        currentCircle.rotate(-placePos)
    currentElf = (currentElf + 1) % numPlayers

print(max(elfScores))