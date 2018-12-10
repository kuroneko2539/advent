import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day7input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

orders = []
for comm in commands:
    orders.append([comm.split(" ")[1], comm.split(" ")[7]])

tree = {}

for pair in orders:
    if pair[1] not in tree.keys():
        tree[pair[1]] = {"dependsOn": [], "leadsTo": []}
    if pair[0] not in tree.keys():
        tree[pair[0]] = {"dependsOn": [], "leadsTo": []}
    tree[pair[1]]["dependsOn"].append(pair[0])
    tree[pair[0]]["leadsTo"].append(pair[1])

workers = {0: {"task": None, "dur": 0}, 1: {"task": None, "dur": 0}, 2: {"task": None, "dur": 0}, 3: {"task": None, "dur": 0}, 4: {"task": None, "dur": 0}}
nextList = []
for key in sorted(list(tree.keys())):
    if len(tree[key]["dependsOn"]) == 0:
        nextList.append(key)
order = ""
totalTime = 0
while True:
    nextList = sorted(nextList)
    added = []
    for toAdd in nextList:
        workerAvail = False
        for worker in workers.keys():
            if workers[worker]["task"] == None: 
                workerAvail = True
                break
        if workerAvail:
            allowed = True
            for dependChar in tree[toAdd]["dependsOn"]:
                if dependChar not in order:
                    allowed = False
                    break
            if allowed: 
                workers[worker]["task"] = toAdd
                added.append(toAdd)
        else:
            break
    for toRem in added:
        del nextList[nextList.index(toRem)]
    for worker in workers.keys():
        if workers[worker]["task"] != None:
            workers[worker]["dur"] += 1
            if workers[worker]["dur"] == (ord(workers[worker]["task"]) - 4):
                order += workers[worker]["task"]
                for nextChar in tree[workers[worker]["task"]]["leadsTo"]:
                    if nextChar not in nextList: nextList.append(nextChar)
                workers[worker] = {"task": None, "dur": 0}
    totalTime += 1
    if len(order) == 26:
        break

print(order)
print(totalTime)