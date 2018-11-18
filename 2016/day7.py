import argparse
import numpy as np
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day7input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    lines = [x.strip() for x in f.readlines()]

goodCount = 0
for line in lines:
    goodLine = True
    startBra, endBra = None, None
    withinBras = []
    for i in range(len(line)):
        if line[i] == "[": startBra = i
        if line[i] == "]": endBra = i
        if startBra and endBra:
            for j in range(startBra + 1, endBra):
                withinBras.append(j)
                startBra, endBra = None, None
    tempLine = line
    while "[" in tempLine:
        endBraInd, startBraInd = None, None
        for i in range(len(tempLine) - 1, -1, -1):
            if tempLine[i] == "]": 
                endBraInd = i
                break
        for i in range(endBraInd, -1, -1):
            if tempLine[i] == "[": 
                startBraInd = i
                break
        if endBraInd and startBraInd:
            for i in range(startBraInd + 1, endBraInd - 3):
                if tempLine[i:i+2] == tempLine[i+3:i+1:-1] and tempLine[i] != tempLine[i+1]: 
                    goodLine = False
            if not goodLine: break
            tempLine = tempLine[:startBraInd] + tempLine[endBraInd + 1:]
    if not goodLine: continue
    goodLine = False
    for i in range(0, len(line) - 3):
        if i in withinBras or i+3 in withinBras: continue
        if line[i:i+2] == line[i+3:i+1:-1] and line[i] != line[i+1]: 
            goodLine = True
    if goodLine: goodCount += 1

print(goodCount)

SSLCount = 0

with open(args.inFile, "r") as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    abas, babs = [], []
    startBra, endBra = None, None
    withinBras = []
    for i in range(len(line)):
        if line[i] == "[": startBra = i
        if line[i] == "]": endBra = i
        if startBra and endBra:
            for j in range(startBra + 1, endBra):
                withinBras.append(j)
                startBra, endBra = None, None
    for i in range(0, len(line) - 2):
        if i in withinBras and i+2 in withinBras:
            if line[i] == line[i+2] and line[i] != line[i+1]:
                babs.append(line[i:i+3])
        elif i not in withinBras and i+2 not in withinBras:
            if line[i] == line[i+2] and line[i] != line[i+1]:
                abas.append(line[i:i+3])
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in babs: 
            SSLCount +=1
            break

print(SSLCount)