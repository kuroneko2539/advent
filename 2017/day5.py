import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day5input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: move direction in list, increment position before leaving

with open(args.inFile, "r") as f:
    inputLines = f.readlines()

inputLines = [int(x) for x in inputLines]

pos = 0
numSteps = 0
while pos >= 0 and pos < len(inputLines):
    changePos = inputLines[pos]
    inputLines[pos] += 1
    pos += changePos
    numSteps += 1
print(numSteps)

##PART 2: if val > 3 decrease, else increase

with open(args.inFile, "r") as f:
    inputLines = f.readlines()

inputLines = [int(x) for x in inputLines]

pos = 0
numSteps = 0
while pos >= 0 and pos < len(inputLines):
    changePos = inputLines[pos]
    if inputLines[pos] > 2: inputLines[pos] -= 1
    else: inputLines[pos] += 1
    pos += changePos
    numSteps += 1
print(numSteps)