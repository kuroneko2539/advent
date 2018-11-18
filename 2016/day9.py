import argparse
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day9input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputString = f.readlines()[0].strip()

outputString = ""
pos = 0

def decompress(inString):
    if "(" not in inString:
        return len(inString)
    lenCount = 0
    while "(" in inString:
        lenCount += inString.find("(")
        inString = inString[inString.find("("):]
        marker = inString[1:inString.find(")")].split("x")
        inString = inString[inString.find(")") + 1:]
        lenCount += decompress(inString[:int(marker[0])]) * int(marker[1])
        inString = inString[int(marker[0]):]
    lenCount += len(inString)
    return lenCount

print(decompress(inputString))