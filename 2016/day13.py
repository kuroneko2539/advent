import copy

inputNumber = 1358

value = 0
locs = [[1,1]]

locations = {str(locs[0]): value}

def getNextLocs(prevLocs):
    nextLocs = []
    for loc in prevLocs:
        x, y = loc[0], loc[1]
        nextLocs.append([x+1,y])
        nextLocs.append([x-1,y])
        nextLocs.append([x,y+1])
        nextLocs.append([x,y-1])
    return nextLocs

def isWall(loc):
    x, y = loc[0], loc[1]
    keyValue = x*x + 3*x + 2*x*y + y + y*y + inputNumber
    asBin = str(bin(keyValue))
    bits = asBin.count("1")
    if bits % 2 == 0:
        return False
    else:
        return True

done = False
while True:
    value += 1
    nextLocs = getNextLocs(locs)
    locs = []
    for loc in nextLocs:
        if loc[0] < 0 or loc[1] < 0: continue
        if str(loc) in locations.keys(): continue
        if isWall(loc):
            continue
        else:
            locations[str(loc)] = value
            locs.append(loc)
            if loc[0] == 31 and loc[1] == 39:
                done = True
                break
    if done: break
    if value == 50: numLocs = len(locations)
    # print(locations)
    # input()
    #print(locations.keys())

print(locations[str([31,39])])

print(numLocs)