import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day11input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: Get shortest distance

with open(args.inFile, "r") as f:
    movements = [x.strip() for x in f.readlines()[0].split(",")]

x, y, z = 0, 0, 0
maxDist = 0

for move in movements:
    if move == "n":
        x -= 1
        y += 1
    if move == "ne":
        y += 1
        z -= 1
    if move == "se":
        x += 1
        z -= 1
    if move == "s":
        x += 1
        y -= 1
    if move == "sw":
        y -= 1
        z += 1
    if move == "nw":
        x -= 1
        z += 1
    if abs(x) > maxDist: maxDist = abs(x)
    if abs(y) > maxDist: maxDist = abs(y)
    if abs(z) > maxDist: maxDist = abs(z)

print(x, y, z)
distance = max([x,y,z])
print(distance)
print(maxDist)