import numpy as np
import hashlib
import copy

#[Gen, Micro]

part = 2

if part == 1:
    currentState = {"eV": 0, "pairs": [[0,1],[0,0],[0,1],[0,0],[0,0]]}
    endState = {"eV": 3, "pairs": [[3,3],[3,3],[3,3],[3,3],[3,3]]}
else:
    currentState = {"eV": 0, "pairs": [[0,1],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0]]}
    endState = {"eV": 3, "pairs": [[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3]]}

visitedStates = []

def getStateHash(state):
    evPos = str(state["eV"])
    sortedStates = sorted(state["pairs"])

    stringState = (evPos + str(sortedStates)).encode("utf-8")

    hashString = hashlib.md5(stringState).hexdigest()
    return hashString

visitedStates.append(getStateHash(currentState))

def checkAllowed(state):
    if state["eV"] < 0 or state["eV"] > 3: 
        #print(state["eV"], "elevator out of bounds")
        return False
    if getStateHash(state) in visitedStates: 
        #print(state["eV"], state["pairs"], "state already visited")
        return False
    pairs = state["pairs"]
    for p in range(len(pairs)):
        if pairs[p][0] == pairs[p][1]: continue
        elif pairs[p][1] in [x[0] for x in pairs]: return False
    visitedStates.append(getStateHash(state))
    return True

def findInPairs(pairs, item):
    locations = []
    for i in range(len(pairs)):
        for j in range(2):
            if pairs[i][j] == item:
                locations.append([i,j])
    return locations

def getNextStates(state):
    nextStates = []
    currentEV = state["eV"]
    currentPairs = state["pairs"]
    
    moveableItems = findInPairs(currentPairs, currentEV)
    # Moving 1 item
    for i in range(len(moveableItems)):
        ##Check move up
        newEV = currentEV + 1
        newPairs = copy.deepcopy(currentPairs)
        newPairs[moveableItems[i][0]][moveableItems[i][1]] = newEV
        newState = {"eV": newEV, "pairs": copy.deepcopy(newPairs)}
        if checkAllowed(newState): nextStates.append(copy.deepcopy(newState))
        ##Check move down
        newEV = currentEV - 1
        newPairs = copy.deepcopy(currentPairs)
        newPairs[moveableItems[i][0]][moveableItems[i][1]] = newEV
        newState = {"eV": newEV, "pairs": copy.deepcopy(newPairs)}
        if checkAllowed(newState): nextStates.append(copy.deepcopy(newState))
    
    # Moving 2 items
    for i in range(len(moveableItems)):
        for j in range(i+1,len(moveableItems)):
            ##Check move up
            newEV = currentEV + 1
            newPairs = copy.deepcopy(currentPairs)
            newPairs[moveableItems[i][0]][moveableItems[i][1]] = newEV
            newPairs[moveableItems[j][0]][moveableItems[j][1]] = newEV
            newState = {"eV": newEV, "pairs": copy.deepcopy(newPairs)}
            if checkAllowed(newState): nextStates.append(copy.deepcopy(newState))
            ##Check move down
            newEV = currentEV - 1
            newPairs = copy.deepcopy(currentPairs)
            newPairs[moveableItems[i][0]][moveableItems[i][1]] = newEV
            newPairs[moveableItems[j][0]][moveableItems[j][1]] = newEV
            newState = {"eV": newEV, "pairs": copy.deepcopy(newPairs)}
            if checkAllowed(newState): nextStates.append(copy.deepcopy(newState))

    return nextStates

nextStates = [currentState]

numSteps = 0
done = False
while True:
    numSteps += 1
    nextNextStates = []
    for state in nextStates:
        nextNextStates += getNextStates(state)
    for state in nextNextStates:
        hashKey = getStateHash(state)
        visitedStates.append(hashKey)
        if hashKey == getStateHash(endState): 
            done = True
            break
    if done:
        break
    else:
        nextStates = copy.deepcopy(nextNextStates)
        print(len(nextStates))
        #input()


print(numSteps)