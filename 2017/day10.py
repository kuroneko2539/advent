import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day10input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: Follow loop round and get first two numbers in final list

with open(args.inFile, "r") as f:
    inputString = f.readlines()[0]

lengths = [int(x.strip()) for x in inputString.split(",")]
#print(lengths)

startListLen = 256

current = list(range(startListLen))
#lengths = [3,4,1,5,0]
start = 0
skip = 0
end = 0
pos = 0

for length in lengths:
    pos = start
    end = (start + length) % startListLen
    if length != 0:
        tempList = []
        while True:
            tempList.append(current[pos])
            pos += 1
            if pos == len(current): pos = 0
            if pos == end: break
        
        tempCount = len(tempList) - 1
        pos = start
        while tempCount > -1:
            current[pos] = tempList[tempCount]
            pos += 1
            if pos == len(current): pos = 0
            tempCount -= 1

    start = end + skip
    start = start % startListLen
    skip += 1

print(current[0] * current[1])
        
##PART 2: Get knothash

with open(args.inFile, "r") as f:
    inputString = f.readlines()[0]



def getKnotHash(inputString):

    lengths = [ord(x) for x in inputString]
    lengths += [17, 31, 73, 47, 23]

    startListLen = 256

    current = list(range(startListLen))
    start = 0
    skip = 0
    end = 0
    pos = 0

    for _ in range(64):
        for length in lengths:
            pos = start
            end = (start + length) % startListLen
            if length != 0:
                tempList = []
                while True:
                    tempList.append(current[pos])
                    pos += 1
                    if pos == len(current): pos = 0
                    if pos == end: break
                
                tempCount = len(tempList) - 1
                pos = start
                while tempCount > -1:
                    current[pos] = tempList[tempCount]
                    pos += 1
                    if pos == len(current): pos = 0
                    tempCount -= 1

            start = end + skip
            start = start % startListLen
            skip += 1

    knothash = []
    for i in range(16):
        currentVal = current[i*16]
        for j in range(15):
            currentVal = currentVal ^ current[i*16+j+1]
        knothash.append(currentVal)

    #print("".join(["{0:0{1}x}".format(x,2) for x in knothash]))

    return("".join(["{0:0{1}x}".format(x,2) for x in knothash]))

print(getKnotHash(inputString))