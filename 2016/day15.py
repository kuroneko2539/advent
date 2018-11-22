import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day15input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    discLines = [line.rstrip() for line in f]

discs = {}

for disc in discLines:
    split = disc.split(" ")
    discs[int(split[1][-1])] = {"posAt0": int(split[-1].split(".")[0]), "numPos": int(split[3])}

def canPassDisc(time, disc):
    posAt0 = disc["posAt0"]
    numPos = disc["numPos"]
    if (posAt0 + time) % numPos == 0:
        return True
    else:
        return False

startT = -1

while True:
    passesThrough = True
    for i in range(len(discs)):
        t = startT + i + 1
        if canPassDisc(t, discs[i+1]): continue
        else: 
            passesThrough = False
            break
    if passesThrough: break
    else: 
        startT += 1

print(startT)
        