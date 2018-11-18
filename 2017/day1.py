import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day1input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputString = f.readlines()[0]

asInts = []
for num in inputString:
    num = int(num)
    asInts.append(num)

##PART 1: Check neighbouring number
outputKey = 0
for i in range(len(asInts)):
    if asInts[i] == asInts[(i + 1) % len(asInts)]: outputKey += asInts[i]

print(outputKey)

##PART 2: Check number halfway around
outputKey = 0
for i in range(len(asInts)):
    if asInts[i] == asInts[(i + int(len(asInts) / 2)) % len(asInts)]: outputKey += asInts[i]

print(outputKey)