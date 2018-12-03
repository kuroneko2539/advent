import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day20input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    blockedList = [x.strip() for x in f.readlines()]

blockedStarts, blockedEnds = [], []

for block in blockedList:
    blockedStarts.append(int(block.split("-")[0]))
    blockedEnds.append(int(block.split("-")[1]))

sortedEnds = sorted(blockedEnds)
sortedStarts = sorted(blockedStarts)

maxSoFar = 0

for i in range(len(sortedStarts)):
    start = sortedStarts[i]
    if start <= maxSoFar + 1:
        index = blockedStarts.index(sortedStarts[i])
        end = blockedEnds[index]
        if end > maxSoFar:
            maxSoFar = end
    else:
        print(maxSoFar + 1)
        break

numAllowed = 0

for i in range(len(sortedStarts)):
    start = sortedStarts[i]
    if start <= maxSoFar + 1:
        index = blockedStarts.index(sortedStarts[i])
        end = blockedEnds[index]
        if end > maxSoFar:
            maxSoFar = end
    else:
        numAllowed += (start - (maxSoFar + 1))
        index = blockedStarts.index(sortedStarts[i])
        end = blockedEnds[index]
        if end > maxSoFar:
            maxSoFar = end
    
print(numAllowed)