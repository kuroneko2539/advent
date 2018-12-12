import argparse, numpy as np, re
import matplotlib.pyplot as plt
import time

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day12input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

transforms = {}
for command in commands:
    split = command.split("=>")
    transforms[split[0].strip()] = split[1].strip()

initialState = "###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#"
zeroID = 0
state = initialState
lastTotal = -456265
lastDifference = -52
sameDiffCount = 0
for p in range(500000000):
    zeroID += 2
    state = ".." + state + ".."
    newState = ""
    for i in range(len(state)):
        if i == 0:
            key = ".." + state[:i+3]
        elif i == 1:
            key = "." + state[i-1:i+3]
        elif i == len(state) - 2:
            key = state[i-2:i+2] + "."
        elif i == len(state) - 1:
            key = state[i-2:i+1] + ".."
        else:
            key = state[i-2:i+3]
        #print(i, state)
        newState += transforms[key]
    state = newState
    total = 0
    for i in range(len(state)):
        val = i - zeroID
        if state[i] == "#": total += val
    if total - lastTotal == lastDifference:
        sameDiffCount += 1
        if sameDiffCount > 10:
            diff = total - lastTotal
            print(diff)
            step = p + 1
            print(step)
            offset = total - step * diff
            print(offset)
            finalVal = diff*50000000000 + offset
            break
    else:
        lastDifference = total - lastTotal
        lastTotal = total

print(finalVal)