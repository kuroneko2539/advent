import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day7input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: find the root of the tower

with open(args.inFile, "r") as f:
    inputLines = f.readlines()

progs = {}
for line in inputLines:
    name = line.split("(")[0].strip()
    weight = int(line[line.find("(")+1:line.find(")")])
    if "->" in line: holding = [x.strip() for x in line.split(" -> ")[1].split(", ")]
    else: holding = None
    progs[name] = {"w": weight, "hold": holding}

for name in progs.keys():
    root = True
    for held in progs.keys():
        if progs[held]["hold"] != None:
            if name in progs[held]["hold"]:
                root = False
                break
    if root: break

rootName = name

##PART 2: find the imbalance

maxDepth = 0
def buildTree(root, depth=0):
    global maxDepth
    if progs[root]["hold"] != None:
        progs[root]["depth"] = depth
        depth += 1
        if depth > maxDepth: maxDepth = depth
        for held in progs[root]["hold"]:
            progs[held]["heldBy"] = root
            buildTree(held, depth)
    else:
        progs[root]["sumWeight"] = progs[root]["w"]
        progs[root]["depth"] = depth

buildTree(rootName)

for depth in range(maxDepth, -1, -1):
    for prog in progs.keys():
        if progs[prog]["depth"] == depth:
            progs[prog]["sumWeight"] = progs[prog]["w"]
            if progs[prog]["hold"] != None:
                for upperprog in progs[prog]["hold"]:
                    progs[prog]["sumWeight"] += progs[upperprog]["sumWeight"]

def findBadWeight(root):
    if progs[root]["hold"] != None:
        weights = []
        for held in progs[root]["hold"]:
            weights.append(progs[held]["sumWeight"])
        if weights.count(weights[0]) != len(weights):
            if weights.count(weights[0]) == len(weights) - 1: print(weights)
            for nextRoot in progs[root]["hold"]:
                print(progs[nextRoot]["w"])
                findBadWeight(nextRoot)


findBadWeight(rootName)