import hashlib

inputSalt = "cuanljph"
index = 0

hashes = {}

def getHashKey(inString):
    encString = inString.encode("utf-8")
    hashKey = hashlib.md5(encString).hexdigest()
    for _ in range(2016):
        hashKey = hashlib.md5(hashKey.encode("utf-8")).hexdigest()
    #print(inString)
    #print(hashKey)
    #print()
    return hashKey

def checkIfKey(index):
    if index in hashes.keys(): hashKey = hashes[index]
    else: 
        hashKey = getHashKey(inputSalt + "{}".format(index))
        hashes[index] = hashKey
    repeatingChar = None
    for i in range(len(hashKey) - 2):
        if hashKey[i] == hashKey[i+1] and hashKey[i] == hashKey[i+2]:
            repeatingChar = hashKey[i]
            break
    if repeatingChar:
        for j in range(1000):
            if (index + j + 1) in hashes.keys(): compareHashKey = hashes[(index + j + 1)]
            else:
                compareHashKey = getHashKey(inputSalt + "{}".format(index + j + 1))
                hashes[(index + j + 1)] = compareHashKey
            for i in range(len(compareHashKey) - 4):
                repeatCount = 0
                for k in range(5):
                    if repeatingChar == compareHashKey[i+k]:
                        repeatCount += 1
                if repeatCount == 5: 
                    return True
        return False
    else:
        return False 
keys = []
while len(keys) < 64:
    if checkIfKey(index): keys.append(index)
    index += 1

print(keys[-1])