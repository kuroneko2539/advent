input_data = [x.strip() for x in open("./day6Input.txt", "r").readlines()]
part = 1

allSatellites = {}

for line in input_data:
    root = line.split(")")[0]
    arm = line.split(")")[1]

    if root in allSatellites.keys():
        allSatellites[root].append(arm)
    else:
        allSatellites[root] = [arm]

root = None
for key in allSatellites.keys():
    foundRoot = True
    for k, v in allSatellites.items():
        if key in v: foundRoot = False
    if foundRoot: root = key

totalSteps = 0
depth = 1

toCheck = allSatellites[root]
reverseSatellites = {}
satelliteValues = {}

while len(toCheck) > 0:
    nextRound = []
    for s in toCheck:
        satelliteValues[s] = depth
        totalSteps += depth
        if s in allSatellites.keys():
            nextRound += allSatellites[s]
            for satellite in allSatellites[s]:
                reverseSatellites[satellite] = s
    depth += 1
    toCheck = nextRound.copy()

print(totalSteps)

fromYOU = []
fromSAN = []

curr = "YOU"
while True:
    if curr in reverseSatellites.keys(): 
        curr = reverseSatellites[curr]
        fromYOU.append(curr)
    else:
        break
curr = "SAN"
while True:
    if curr in reverseSatellites.keys(): 
        curr = reverseSatellites[curr]
        fromSAN.append(curr)
    else:
        break

inBoth = set(fromYOU).intersection(set(fromSAN))
valsInBoth = [satelliteValues[x] for x in inBoth]
print(max(valsInBoth), satelliteValues["YOU"], satelliteValues["SAN"])
print((satelliteValues["YOU"]-max(valsInBoth)) + (satelliteValues["SAN"]-max(valsInBoth)) - 2)