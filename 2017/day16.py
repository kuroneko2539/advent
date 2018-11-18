import argparse
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day16input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: Get shortest distance

with open(args.inFile, "r") as f:
    movements = [x.strip() for x in f.readlines()[0].split(",")]

positions = deque([x for x in "abcdefghijklmnop"])

for movement in movements:
    if movement[0] == "s":
        rotate = int(movement.split("s")[1])
        positions.rotate(rotate)
    if movement[0] == "x":
        pos0, pos1 = [int(x) for x in movement[1:].split("/")]
        toPos0, toPos1 = positions[pos1], positions[pos0]
        positions[pos0] = toPos0
        positions[pos1] = toPos1
    if movement[0] == "p":
        pos0, pos1 = [positions.index(x) for x in movement[1:].split("/")]
        toPos0, toPos1 = positions[pos1], positions[pos0]
        positions[pos0] = toPos0
        positions[pos1] = toPos1

print("".join(positions))

positions = deque([x for x in "abcdefghijklmnop"])

for i in range(1000000000):
    for movement in movements:
        if movement[0] == "s":
            rotate = int(movement.split("s")[1])
            positions.rotate(rotate)
        if movement[0] == "x":
            pos0, pos1 = [int(x) for x in movement[1:].split("/")]
            toPos0, toPos1 = positions[pos1], positions[pos0]
            positions[pos0] = toPos0
            positions[pos1] = toPos1
        if movement[0] == "p":
            pos0, pos1 = [positions.index(x) for x in movement[1:].split("/")]
            toPos0, toPos1 = positions[pos1], positions[pos0]
            positions[pos0] = toPos0
            positions[pos1] = toPos1
    if positions == deque([x for x in "abcdefghijklmnop"]):
        print(i + 1)
        cycle = i + 1
        break

positions = deque([x for x in "abcdefghijklmnop"])
for i in range(1000000000 % cycle):
    for movement in movements:
        if movement[0] == "s":
            rotate = int(movement.split("s")[1])
            positions.rotate(rotate)
        if movement[0] == "x":
            pos0, pos1 = [int(x) for x in movement[1:].split("/")]
            toPos0, toPos1 = positions[pos1], positions[pos0]
            positions[pos0] = toPos0
            positions[pos1] = toPos1
        if movement[0] == "p":
            pos0, pos1 = [positions.index(x) for x in movement[1:].split("/")]
            toPos0, toPos1 = positions[pos1], positions[pos0]
            positions[pos0] = toPos0
            positions[pos1] = toPos1

print("".join(positions))