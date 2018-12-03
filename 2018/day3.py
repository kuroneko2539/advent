import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day3input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    patches = [x.strip() for x in f.readlines()]

squareUse = {}

for patch in patches:
    split = patch.split("@")[1]

    startCoords = split.split(":")[0]
    dims = split.split(":")[1]

    xStart,yStart = int(startCoords.split(",")[0]), int(startCoords.split(",")[1])
    width,height = int(dims.split("x")[0]), int(dims.split("x")[1])

    for i in range(width):
        for j in range(height):
            if (xStart + i, yStart + j) in squareUse.keys():
                squareUse[(xStart + i, yStart + j)] += 1
            else:
                squareUse[(xStart + i, yStart + j)] = 1

greaterThanOne = 0
for i in squareUse.keys():
    if squareUse[i] > 1:
        greaterThanOne += 1
print(greaterThanOne)

for patch in patches:
    split = patch.split("@")[1]

    startCoords = split.split(":")[0]
    dims = split.split(":")[1]

    xStart,yStart = int(startCoords.split(",")[0]), int(startCoords.split(",")[1])
    width,height = int(dims.split("x")[0]), int(dims.split("x")[1])

    patchCount = 0
    for i in range(width):
        for j in range(height):
            if squareUse[(xStart + i, yStart + j)] == 1:
                patchCount += 1
    if patchCount == width * height:
        print(patch)