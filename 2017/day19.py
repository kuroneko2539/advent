import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day19input.txt", help="file containing input key")
args = parser.parse_args()

grid = []
with open(args.inFile, "r") as f:
    temprows = f.readlines()
    for row in temprows:
        grid.append([x.strip() for x in row])

j,i = 0, grid[0].index("|")
direction = (1,0)

result = []
nextSpace = None
stepCount = 0

while True:
    stepCount += 1
    j += direction[0]
    i += direction[1]
    nextSpace = grid[j][i]
    if nextSpace == "":
        break
    elif nextSpace != "+":
        if str.isalpha(nextSpace):
            result.append(nextSpace)
    else:
        oldDirection = direction
        if abs(direction[0]) == 1:
            if i > 0:
                if grid[j][i - 1] not in ["|",""]:
                    direction = (0,-1)
            if i < len(grid[j]) - 1:
                if grid[j][i + 1] not in ["|",""]:
                    direction = (0,1)
        else:
            if j > 0:
                if grid[j - 1][i] not in ["-",""]:
                    direction = (-1,0)
            if j < len(grid) - 1:
                if grid[j + 1][i] not in ["-",""]:
                    direction = (1,0)
        if direction == oldDirection:
            break
print("".join(result))
print(stepCount)