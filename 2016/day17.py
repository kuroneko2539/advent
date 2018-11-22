import hashlib
import copy

inputKey = "bwnlcvfs"

def getNextMoves(currentMoves):
    nextMoves = []
    toHash = (inputKey + currentMoves).encode("utf-8")
    hashKey = hashlib.md5(toHash).hexdigest()
    for i in range(4):
        if hashKey[i] in ["b","c","d","e","f"]:
            if i == 0:
                nextMoves.append("U")
            if i == 1:
                nextMoves.append("D")
            if i == 2:
                nextMoves.append("L")
            if i == 3:
                nextMoves.append("R")
    return nextMoves

pos = [0, 0]

currentMoves = [["", pos]]
done = False
reachesEnd = []

while True:
    nextMoves = []
    if len(currentMoves) == 0:
        break
    for moves in currentMoves:
        posX, posY = moves[1][0], moves[1][1]
        movesToDate = moves[0]
        possibleMoves = getNextMoves(movesToDate)
        for move in possibleMoves:
            newX, newY = posX, posY
            if move == "U":
                newY = posY - 1
                if newY != -1:
                    nextMoves.append([movesToDate + move, [posX,newY]])
            if move == "D":
                newY = posY + 1
                if newY != 4:
                    nextMoves.append([movesToDate + move, [posX,newY]])
            if move == "L":
                newX = posX - 1
                if newX != -1:
                    nextMoves.append([movesToDate + move, [newX,posY]])
            if move == "R":
                newX = posX + 1
                if newX != 4:
                    nextMoves.append([movesToDate + move, [newX,posY]])
            if newX == 3 and newY == 3:
                reachesEnd.append(copy.deepcopy(nextMoves[-1]))
                del nextMoves[-1]
                #done = True
                #break
        #if done: break
    #if done: break
    currentMoves = copy.deepcopy(nextMoves)

print(len(reachesEnd[-1][0]))