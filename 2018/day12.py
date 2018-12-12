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
    if state.count("#") == 34:
        total = 0
        for i in range(len(state)):
            val = i - zeroID
            if state[i] == "#": total += val
        print(p, total)
        input()

total = 0
for i in range(len(state)):
    val = i - zeroID
    if state[i] == "#": total += val
print(total)