import argparse
import numpy as np
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day21input.txt", help="file containing input key")
args = parser.parse_args()

def getStringFromArray(inArray):
    string = ""
    for i in range(inArray.shape[0]):
        for j in range(inArray.shape[1]):
            string += inArray[i,j]
        string += "/"
    return string[:-1]

def getArrayFromString(inString):
    rows = inString.split("/")
    for row in range(len(rows)):
        rows[row] = [x for x in rows[row]]
    return np.array(rows)

rules = {}
with open(args.inFile, "r") as f:
    ruleLines = [line.rstrip() for line in f]
    for line in ruleLines:
        lineRules = []
        inPat = line.split(" => ")[0]
        outPat = line.split(" => ")[1]
        inPatArray = getArrayFromString(inPat)
        for flip in ["N","FLR","FUD"]:
            for rot in ["0","90","180","270"]:
                currentRule = inPatArray.copy()
                if flip == "FLR": currentRule = np.fliplr(currentRule)
                elif flip == "FUD": currentRule = np.flipud(currentRule)

                if rot == "90": currentRule = np.rot90(currentRule, k=1)
                elif rot == "180": currentRule = np.rot90(currentRule, k=2)
                elif rot == "270": currentRule = np.rot90(currentRule, k=3)
                storeRule = getStringFromArray(currentRule)
                if storeRule not in lineRules: lineRules.append(storeRule)
        
        for rule in lineRules:
            rules[rule] = outPat

initialPattern = ".#./..#/###"

a = getArrayFromString(initialPattern)

def iterateImage(imageArray):
    if imageArray.shape[0] % 2 == 0:
        newArrayDims = imageArray.shape[0] + int(imageArray.shape[0] / 2)
        newArray = np.empty(shape=(newArrayDims,newArrayDims), dtype="<U1")

        for i in range(int(imageArray.shape[0] / 2)):
            for j in range(int(imageArray.shape[0] / 2)):
                block = imageArray[2*i:2*i+2,2*j:2*j+2]
                string = getStringFromArray(block)
                newString = rules[string]
                newBlock = getArrayFromString(newString)
                newArray[3*i:3*i+3,3*j:3*j+3] = newBlock

    else:
        newArrayDims = imageArray.shape[0] + int(imageArray.shape[0] / 3)
        newArray = np.empty(shape=(newArrayDims,newArrayDims), dtype="<U1")

        for i in range(int(imageArray.shape[0] / 3)):
            for j in range(int(imageArray.shape[0] / 3)):
                block = imageArray[3*i:3*i+3,3*j:3*j+3]
                string = getStringFromArray(block)
                newString = rules[string]
                newBlock = getArrayFromString(newString)
                newArray[4*i:4*i+4,4*j:4*j+4] = newBlock
    
    return newArray

for i in range(18):
    print(a)
    a = iterateImage(a)

print(np.count_nonzero(a == "#"))