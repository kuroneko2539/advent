inputKey = "11011110011011101"

def getNextDragonCurve(key):
    a = key
    b = ""
    for i in range(len(a) - 1, -1, -1):
        if a[i] == "0":
            b += "1"
        else:
            b += "0"
    newKey = a + "0" + b
    return newKey

def getDragonCurveForDisk(key, diskSize):
    currentKey = key
    while len(currentKey) < diskSize:
        currentKey = getNextDragonCurve(currentKey)
    return currentKey[0:diskSize]

def calcChecksum(key):
    checksum = ""
    for i in range(int(len(key) / 2)):
        if key[2*i] == key[2*i + 1]: checksum += "1"
        else: checksum += "0"
    return checksum

def getFinalChecksum(key):
    currentChecksum = calcChecksum(key)
    while len(currentChecksum) % 2 == 0:
        currentChecksum = calcChecksum(currentChecksum)
    return currentChecksum

print(getFinalChecksum(getDragonCurveForDisk(inputKey, 35651584)))
