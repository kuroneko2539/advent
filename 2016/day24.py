import argparse
from collections import deque
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day24input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

targets = {}
distances = {}
paths1 = []
paths2 = []
directions  = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j].isdigit():
            targets[int(grid[i][j])] = (i, j)


def allowedMove(i, j):
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] in ".0123456789":
        return True
    else:
        return False
  
for target, position in targets.items():
    paths = deque([[position]])
    seen = set()
    seen.add(position)
    while paths:
        curr_path = paths.popleft()
        i, j = curr_path[-1]
        if (i, j) in targets.values() and len(curr_path) > 1:
            distances[(target, int(grid[i][j]))] = len(curr_path) - 1
            continue
        for x, y in directions:
            if allowedMove(i + x, j + y) and (i + x, j + y) not in seen:
                paths.append(curr_path + [(i + x, j + y)])
                seen.add((i + x, j + y))


for path in itertools.permutations(range(1, 8)):
    path = (0,) + path + (0,)
    distance = 0
    for i in range(len(path) - 2):
        distance += distances[(path[i], path[i+1])]
    paths1.append(distance)
    paths2.append(distance + distances[(path[-2], path[-1])])

print(min(paths1))
print(min(paths2))