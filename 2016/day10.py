import argparse
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day10input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    lines = [x.strip() for x in f.readlines()]

robots = {}
outputs = {}
for line in lines:
    split = line.split(" ")
    for word in range(len(split)):
        if split[word] == "bot":
            robots[split[word+1]] = {"holding": [], "giveHighBot": True, "giveHigh": None, "giveLowBot": True, "giveLow": None}
        if split[word] == "output":
            outputs[split[word + 1]] = {"contains": []}

for line in lines:
    split = line.split(" ")
    if split[0] == "value":
        robots[split[-1]]["holding"].append(int(split[1]))
    if split[0] == "bot":
        robot = split[1]
        if split[5] != "bot": robots[robot]["giveLowBot"] = False
        robots[robot]["giveLow"] = split[6]
        if split[-2] != "bot": robots[robot]["giveHighBot"] = False
        robots[robot]["giveHigh"] = split[-1]

found = False
part = 2
while not found:
    for robot in robots.keys():
        if len(robots[robot]["holding"]) > 1:
            high = max(robots[robot]["holding"])
            low = min(robots[robot]["holding"])
            giveHigh = robots[robot]["giveHigh"]
            giveLow = robots[robot]["giveLow"]

            if robots[robot]["giveHighBot"]: 
                robots[giveHigh]["holding"].append(high)
            else:
                outputs[giveHigh]["contains"].append(high)
            if robots[robot]["giveLowBot"]: 
                robots[giveLow]["holding"].append(low)
            else:
                outputs[giveLow]["contains"].append(low)

            if part == 1:
                if 61 in robots[giveHigh]["holding"] and 17 in robots[giveHigh]["holding"]: 
                    found = True
                    print(giveHigh)
                if 61 in robots[giveLow]["holding"] and 17 in robots[giveLow]["holding"]: 
                    found = True
                    print(giveLow)
            if part == 2:
                if len(outputs["0"]["contains"]) > 0 and len(outputs["1"]["contains"]) > 0 and len(outputs["2"]["contains"]) > 0:
                    print(outputs["0"]["contains"][0]*outputs["1"]["contains"][0]*outputs["2"]["contains"][0])
                    found = True