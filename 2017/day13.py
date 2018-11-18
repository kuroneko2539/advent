import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day13input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputLines = [line.strip() for line in f.readlines()]

scanners = {}
colsWithScanners = []
for line in inputLines:
    split = line.split(": ")
    colsWithScanners.append(int(split[0]))
    scanners[int(split[0])] = {"pos": 0, "len": int(split[1]), "mode": "inc"}
    numCols = int(split[0])

print(numCols)
pos = -1
severity = 10
pause = 0

""" while severity > 0:
    severity = 0
    for scanner in colsWithScanners:
        scanners[scanner]["pos"] = 0
        scanners[scanner]["mode"] = "inc"
    pos = -1 - pause
    while pos < numCols:
        pos += 1
        if pos in colsWithScanners:
            if scanners[pos]["pos"] == 0:
                #print(pos)
                severity += pos * scanners[pos]["len"]
        for scanner in colsWithScanners:
            if scanners[scanner]["mode"] == "inc":
                scanners[scanner]["pos"] += 1
                if scanners[scanner]["pos"] == scanners[scanner]["len"] - 1: scanners[scanner]["mode"] = "dec"
            elif scanners[scanner]["mode"] == "dec":
                scanners[scanner]["pos"] -= 1
                if scanners[scanner]["pos"] == 0: scanners[scanner]["mode"] = "inc"
    pause += 2
    

print(pause) """
delay = 0
while True:
    done = True
    for scanner in colsWithScanners:
        if (scanner + delay) % (2 * (scanners[scanner]["len"] - 1)) == 0:
            delay += 1
            done = False
            break
    if done: break
        
print(delay)