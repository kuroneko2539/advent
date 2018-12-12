import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day3Input.txt", help="file contianing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inString = [x.strip() for x in f.readlines()][0]

coordChanges = {"^": [0,1], ">": [1,0], "<": [-1,0], "v": [0,-1]}

part = 2

if part == 1:
    pos = [0,0]
    presents = {(0,0): 1}

    for i in range(len(inString)):
        direction = coordChanges[inString[i]]
        pos[0] += direction[0]
        pos[1] += direction[1]
        key = (pos[0], pos[1])

        if key in presents.keys():
            presents[key] += 1
        else:
            presents[key] = 1

    print(len(presents))
else:
    pos = [[0,0], [0,0]]
    presents = {(0,0): 1}
    currentMove = 0

    for i in range(len(inString)):
        direction = coordChanges[inString[i]]
        pos[currentMove][0] += direction[0]
        pos[currentMove][1] += direction[1]
        key = (pos[currentMove][0], pos[currentMove][1])

        if key in presents.keys():
            presents[key] += 1
        else:
            presents[key] = 1

        currentMove = (currentMove + 1) % 2

    print(len(presents))