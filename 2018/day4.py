import argparse, re

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day4input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

commandList = []
for command in commands:
    dateTime = re.findall("\[.*?\]",command)[0]
    com = command.split("]")[1].lstrip().rstrip()
    commandList.append([dateTime, com])

sortedList = sorted(commandList, key=lambda x: x[0])

guards = {}
maxMins = 0
for com in sortedList:
    print(com)
    if "Guard" in com[1]:
        ID = com[1].split("#")[1].split(" ")[0]
        if ID not in guards.keys():
            guards[ID] = {"minsAsleep": 0, "specificMins": []}
    if "falls" in com[1]:
        start = int(com[0][-6:-4]) * 60 + int(com[0][-3:-1])
    if "wakes" in com[1]:
        end = int(com[0][-6:-4]) * 60 + int(com[0][-3:-1])
        guards[ID]["minsAsleep"] += (end-start)
        if guards[ID]["minsAsleep"] > maxMins:
            maxMins = guards[ID]["minsAsleep"]
            maxID = ID
        guards[ID]["specificMins"] += list(range(start,end))
print(maxID)
print(guards[maxID])
print(max(set(guards[maxID]["specificMins"]), key=guards[maxID]["specificMins"].count))

maxCount = 0
finalID = None
finalMin = None
for guard in guards.keys():
    if guards[guard]["minsAsleep"] == 0: continue
    minute = max(set(guards[guard]["specificMins"]), key=guards[guard]["specificMins"].count)
    count = guards[guard]["specificMins"].count(minute)
    if count > maxCount:
        maxCount = count
        finalID = guard
        finalMin = minute

print(finalID, finalMin, finalID*finalMin)
        

