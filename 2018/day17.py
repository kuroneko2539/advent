import argparse, numpy as np
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day17input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

minY = 500
maxY = 0
clayCoords = []
for command in commands:
    if command[0] == "x":
        x = int(command.split("=")[1].split(",")[0])
        split = command.split("=")[2]
        start, end = int(split.split("..")[0]), int(split.split("..")[1])
        for i in range(start, end+1):
            clayCoords.append([x,i])
            if i < minY: minY = i
            if i > maxY: maxY = i
    else:
        y = int(command.split("=")[1].split(",")[0])
        if y < minY: minY = y
        if y > maxY: maxY = y
        split = command.split("=")[2]
        start, end = int(split.split("..")[0]), int(split.split("..")[1])
        for i in range(start, end+1):
            clayCoords.append([i,y])

## Empty = 0, water = 1, clay = 2
grid = np.zeros((1000,maxY+1))
for coord in clayCoords:
    grid[coord[0],coord[1]] = 2
#source at (500,0)
with open("./grid.txt", "w") as f:
    for j in range(grid.shape[1]):
        for i in range(grid.shape[0]):
            if grid[i,j] == 0:
                f.write(".")
            if grid[i,j] == 2:
                f.write("#")
        f.write("\n")

pos = [500,0]
# COMPLETED BY HAND

# def getNextSources(source):
#     global grid
#     downSources = []
#     sideSources = []
#     sourcePos = source.copy()
#     if False:#grid[sourcePos[0],sourcePos[1]] == 1:
#         return None
#     else:
#         currentPos = source.copy()
#         checkDown = True
#         while checkDown:
#             grid[currentPos[0],currentPos[1]] = 1
#             if grid[currentPos[0],currentPos[1] + 1] == 2:
#                 checkDown = False
#             elif grid[currentPos[0],currentPos[1] + 1] == 1:
#                 checkLeft = True
#                 left = 1
#                 while checkLeft:
#                     if grid[currentPos[0] - left,currentPos[1] + 1] == 0:
#                         if grid[currentPos[0] - left + 1,currentPos[1] + 1] == 1:
#                             return None
#                     elif grid[currentPos[0] - left,currentPos[1]] == 2:
#                         checkLeft = False
#                     left += 1
                
#                 checkRight = True
#                 right = 1
#                 while checkRight:
#                     if grid[currentPos[0] + right,currentPos[1] + 1] == 0:
#                         if grid[currentPos[0] + right - 1,currentPos[1] + 1] == 1:
#                             return None
#                     elif grid[currentPos[0] + right,currentPos[1]] == 2:
#                         checkRight = False
#                     right += 1
#                 checkDown = False
#             else:
#                 currentPos[1] += 1
#                 if currentPos[1] > maxY:
#                     return None

#         checkLeft = True
#         left = 1
#         while checkLeft:
#             if grid[currentPos[0]-left,currentPos[1]+1] == 0:
#                 downSources.append([currentPos[0]-left,currentPos[1]])
#                 checkLeft = False
#             elif grid[currentPos[0]-left,currentPos[1]] == 2:
#                 sideSources.append([currentPos[0]-left+1,currentPos[1]-1])
#                 checkLeft = False
#             else:
#                 grid[currentPos[0]-left,currentPos[1]] = 1
#             left += 1
#         checkRight = True
#         right = 1
#         while checkRight:
#             if grid[currentPos[0]+right,currentPos[1]+1] == 0:
#                 downSources.append([currentPos[0]+right,currentPos[1]])
#                 checkRight = False
#             elif grid[currentPos[0]+right,currentPos[1]] == 2:
#                 sideSources.append([currentPos[0]+right-1,currentPos[1]-1])
#                 checkRight = False
#             else:
#                 grid[currentPos[0]+right,currentPos[1]] = 1
#             right += 1
#         if len(downSources) == 0:
#             return sideSources
#         else:
#             return downSources
            

# sources = [[500,0]]
# print(minY, maxY)

# while len(sources) > 0:
#     nextSources = []
#     for source in sources:
#         nextS = getNextSources(source)
#         if nextS:
#             for x in nextS:
#                 nextSources.append(x)
#     sources = nextSources.copy()
#     plt.imshow(np.rot90(grid, axes=(1,0)))
#     plt.show()
#     plt.close()


# print(np.sum(np.where(grid == 1)))
# plt.imshow(np.rot90(grid, axes=(1,0)))
# plt.show()
# plt.close()