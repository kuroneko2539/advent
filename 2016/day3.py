import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day3input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    triangles = []
    lines = f.readlines()
    for col in [0,1,2]:
        triangle = []
        for line in lines:
            triangle.append(int(line.split()[col].strip()))
            if len(triangle) == 3:
                triangles.append(triangle.copy())
                triangle = []

goodTriangles = 0

for triangle in triangles:
    good = True
    for perm in [[0,1,2],[0,2,1],[1,2,0]]:
        if triangle[perm[0]] + triangle[perm[1]] <= triangle[perm[2]]:
            good = False
            break
    if good: goodTriangles += 1

print(goodTriangles)