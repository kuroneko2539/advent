input_data = [x.strip() for x in open("./day4Input.txt", "r").readlines()]
part = 2
minR = int(input_data[0].split("-")[0])
maxR = int(input_data[0].split("-")[1])

print(minR, maxR)

def checkAcceptable(value, part):
    twoNext = False
    Asc = True
    stringVal = str(value)
    if part == 1:
        for i in range(len(stringVal) - 1):
            if stringVal[i] == stringVal[i+1]: twoNext = True
            if int(stringVal[i]) > int(stringVal[i+1]): Asc = False
    elif part == 2:
        for i in range(len(stringVal) - 1):
            if int(stringVal[i]) > int(stringVal[i+1]): Asc = False
        setVal = set([x for x in stringVal])
        for val in setVal:
            if stringVal.count(val) == 2: twoNext = True
        

    if Asc and twoNext: return True
    else: return False

accepatable = 0

for i in range(minR, maxR+1):
    if checkAcceptable(i, part): accepatable+=1

print(accepatable)