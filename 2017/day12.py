import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day12input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    connections = [line.rstrip() for line in f]

fullList = {}
for connection in connections:
    split = connection.split(" <-> ")
    fromNode = split[0].strip()
    toNodes = [x.strip() for x in split[1].split(",")]
    fullList[fromNode] = {"toNodes": toNodes}

inList = []

def getNumConnected(root):
    global inList
    inList.append(int(root))
    for node in fullList[root]["toNodes"]:
        if int(node) in inList: continue
        else:
            getNumConnected(node)

getNumConnected("0")
print(len(inList))

numGroups = 0
currentStart = "0"
inList = []
run = True
while True:
    inList = sorted(inList)
    for i in range(len(inList) - 1):
        run = True
        if int(inList[i+1]) - int(inList[i]) != 1:
            currentStart = str(int(inList[i]) + 1)
            break
        run = False
    if run:
        numGroups += 1
        getNumConnected(currentStart)
    else:
        break
    
print(numGroups)