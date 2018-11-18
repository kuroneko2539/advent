import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day24input.txt", help="file containing input key")
args = parser.parse_args()

parts = []

with open(args.inFile, "r") as f:
    partLines = [line.rstrip().split("/") for line in f]
    for line in partLines:
        parts.append([int(x) for x in line])

def getPossibleNexts(currentEnd, remainingParts):
    possibleNexts = []
    for part in remainingParts:
        if currentEnd in part:
            possibleNexts.append(part)
    return possibleNexts

currentEnd = 0
remainingParts = parts.copy()
currentParts = []
toProcess = []
finalBridges = []

toProcess.append([currentEnd, remainingParts, currentParts])

while len(toProcess) > 0:
    toProcessNext = []
    for bridge in toProcess:
        possibleNexts = getPossibleNexts(bridge[0], bridge[1])
        if len(possibleNexts) > 0:
            for possible in possibleNexts:
                if possible.index(bridge[0]) == 0:
                    currentEnd = possible[1]
                else:
                    currentEnd = possible[0]
                remainingParts = bridge[1].copy()
                del remainingParts[remainingParts.index(possible)]
                currentParts = bridge[2].copy()
                currentParts.append(possible)
                toProcessNext.append([currentEnd, remainingParts, currentParts])
        else:
            finalBridges.append(bridge[2].copy())
    toProcess = toProcessNext.copy()

maxStrength = 0
maxLen = 0
maxLenStrength = 0
for bridge in finalBridges:
    strength =  sum([x[0] + x[1] for x in bridge])
    if len(bridge) > maxLen and strength > maxLenStrength:
        maxLen = len(bridge)
        maxLenStrength = strength
    if strength > maxStrength: maxStrength = strength

print(maxStrength)
print(maxLen, maxLenStrength)