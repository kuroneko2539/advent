import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day9input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputString = f.readlines()[0]

##PART 1&2: Calculate score for all and amount of garbage

pos = 0
inTrash = False
trashStart, trashEnd = None, None
trashGroups = []
totalGarbage = 0
#remove trash
while True:
    if inTrash:
        if inputString[pos] == ">":
            trashEnd = pos
            inTrash = False
            trashGroups.append((trashStart, trashEnd))
            trashStart, trashEnd = None, None
        elif inputString[pos] == "!":
            pos += 2
        else:
            totalGarbage += 1
            pos += 1
    else:
        if inputString[pos] == "<":
            trashStart = pos
            inTrash = True
        if inputString[pos] == "!":
            pos += 2
        else:
            pos += 1
    if pos == len(inputString): break

trashless = inputString
for group in range(len(trashGroups) - 1, -1, -1):
    trashless = trashless[:trashGroups[group][0]] + trashless[trashGroups[group][1] + 1:]

currentDepth = 1
totalScore = 0
for i in range(len(trashless)):
    if trashless[i] == "{":
        totalScore += currentDepth
        currentDepth += 1
    elif trashless[i] == "}":
        currentDepth -= 1
print(totalScore)
print(totalGarbage)