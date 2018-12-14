import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day6Input.txt", help="file contianing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

grid = np.zeros((1000,1000), dtype=np.int)

part = 2

for command in commands:
    split = command.split(" ")
    if split[0] == "turn":
        tLX, tLY, bRX, bRY = int(split[2].split(",")[0]), int(split[2].split(",")[1]), int(split[4].split(",")[0]), int(split[4].split(",")[1])
        if split[1] == "on":
            for i in range(tLX, bRX+1):
                for j in range(tLY, bRY+1):
                    if part == 1:
                        grid[i,j] = 1
                    else:
                        grid[i,j] += 1
        else:
            for i in range(tLX, bRX+1):
                for j in range(tLY, bRY+1):
                    if part == 1:
                        grid[i,j] = 0
                    else:
                        grid[i,j] -= 1
                        if grid[i,j] < 0: grid[i,j] = 0
    else:
        tLX, tLY, bRX, bRY = int(split[1].split(",")[0]), int(split[1].split(",")[1]), int(split[3].split(",")[0]), int(split[3].split(",")[1])
        for i in range(tLX, bRX+1):
                for j in range(tLY, bRY+1):
                    if part == 1:
                        grid[i,j] = (grid[i,j] + 1) % 2
                    else:
                        grid[i,j] += 2
print(np.sum(grid))