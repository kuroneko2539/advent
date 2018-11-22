import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day18input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    baseRowIn = f.readline()

gridWidth = len(baseRowIn) + 2
print(gridWidth)
grid = np.zeros((400000,gridWidth))

for i in range(1,gridWidth-1):
    charVal = baseRowIn[i-1]
    if charVal != ".":
        grid[0,i] = 1

# rowsSeen = [str(grid[0])]
for i in range(1,400000):
    for j in range(1,gridWidth-1):
        left = grid[i-1,j-1]
        centre = grid[i-1,j]
        right = grid[i-1,j+1]
        if left and centre and not right: grid[i,j] = 1
        if not left and centre and right: grid[i,j] = 1
        if left and not centre and not right: grid[i,j] = 1
        if not left and not centre and right: grid[i,j] = 1

    # if str(grid[i]) not in rowsSeen: rowsSeen.append(str(grid[i]))
    # else:
    #     print(rowsSeen.index(str(grid[i])))
    #     print(i)
    #     input()

#print(((gridWidth - 2) * 40) - int(np.sum(grid)))
print(((gridWidth - 2) * 400000) - int(np.sum(grid)))