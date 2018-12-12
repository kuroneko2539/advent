import hashlib

inputKey = "ckczppom"
val = 0
part = 1

while True:
    val += 1
    key = inputKey + str(val)

    hash = hashlib.md5(key.encode("utf-8")).hexdigest()
    if part == 1:
        if hash[:5] == "00000": 
            print(val)
            break
    else:
        if hash[:6] == "000000": 
            print(val)
            break