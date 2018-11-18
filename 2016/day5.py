import hashlib

roomID = "ffykfhsq"

loopCount = 0
finalKey = ["_","_","_","_","_","_","_","_"]
while True:
    hashIn = bytes("{}{}".format(roomID, loopCount).encode("utf-8"))
    hashkey = hashlib.md5(hashIn).hexdigest()
    if hashkey[0:5] == "00000": 
        if hashkey[5] in ["0","1","2","3","4","5","6","7"]:
            pos = int(hashkey[5])
            if finalKey[pos] == "_":
                finalKey[pos] = hashkey[6]
                print(finalKey)
    if "_" not in finalKey: break
    loopCount += 1

print(finalKey)