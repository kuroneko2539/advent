import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day5Input.txt", help="file contianing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    strings = [x.strip() for x in f.readlines()]

def isNiceP1(inStr):
    if any(x in inStr for x in ["ab", "cd", "pq", "xy"]): return False
    elif (inStr.count("a") + inStr.count("e") + inStr.count("i") + inStr.count("o") + inStr.count("u")) > 2:
        for i in range(len(inStr) - 1):
            if inStr[i] == inStr[i+1]: return True
    return False

def isNiceP2(inStr):
    twoPairs, singleSepPair = False, False

    for i in range(len(inStr) - 3):
        pairA = inStr[i:i+2]
        for j in range(i+2, len(inStr)):
            pairB = inStr[j:j+2]
            if pairA == pairB:
                twoPairs = True
                break
        if twoPairs:
            break
    
    for i in range(len(inStr) - 2):
        if inStr[i] == inStr[i+2] and inStr[i] != inStr[i+1]: singleSepPair = True
        if singleSepPair: break

    return (twoPairs and singleSepPair)

niceP1Count = 0
niceP2Count = 0
for string in strings:
    if isNiceP1(string): niceP1Count += 1
    if isNiceP2(string): niceP2Count += 1
print(niceP1Count, niceP2Count)