import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day1input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    movements = [x.strip() for x in f.readlines()[0].split(",")]
    movements = [[x[0], int(x[1:])] for x in movements]

directions = [[0,1], [1,0], [0,-1], [-1,0]]
direction = 0
pos = [0,0]
visited = [[0,0]]

stop = False

for movement in movements:
    if movement[0] == "R":
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4
    for _ in range(movement[1]):
        pos[0] += directions[direction][0]
        pos[1] += directions[direction][1]
        print(pos)
        if pos in visited: 
            stop = True
            break
        visited.append(pos.copy())
    if stop: break

print(pos)
print(sum([abs(x) for x in pos]))