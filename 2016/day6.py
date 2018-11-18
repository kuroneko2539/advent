import argparse
import numpy as np
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day6input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    lines = [x.strip() for x in f.readlines()]

columns = []
for _ in range(len(lines[0])):
    columns.append([])

print(len(columns))
for line in lines:
    for i in range(len(line)):
        columns[i].append(line[i])

highestProbWord = ""
lowestProbWord = ""

for column in columns:
    count = Counter(column)
    highestProb = count.most_common(1)
    lowestProb = count.most_common()[-1]
    highestProbWord += highestProb[0][0]
    lowestProbWord += lowestProb[0][0]

print(highestProbWord)
print(lowestProbWord)