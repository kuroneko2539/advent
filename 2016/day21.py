import argparse, numpy as np
from collections import deque
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day21input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

password = deque("abcdefgh")

for command in commands:
    split = command.split(" ")
    if split[0] == "swap" and split[1] == "position":
        pos1, pos2 = int(split[2]), int(split[5])
        x, y = password[pos1], password[pos2]
        password[pos1] = y
        password[pos2] = x
    if split[0] == "swap" and split[1] == "letter":
        let1, let2 = split[2], split[5]
        pos1, pos2 = password.index(let1), password.index(let2)
        password[pos1] = let2
        password[pos2] = let1
    if split[0] == "rotate" and split[1] == "right":
        steps = int(split[2])
        password.rotate(steps)
    if split[0] == "rotate" and split[1] == "left":
        steps = -int(split[2])
        password.rotate(steps)
    if split[0] == "rotate" and split[1] == "based":
        let1 = split[6]
        index = password.index(let1)
        password.rotate(1)
        password.rotate(index)
        if index > 3: password.rotate(1)
    if split[0] == "reverse":
        start, end = int(split[2]), int(split[4])
        toReplace = []
        for i in range(end, start-1, -1):
            toReplace.append(password[i])
        for i in range(start, end+1):
            password[i] = toReplace[i - start]
    if split[0] == "move":
        pos1, pos2 = int(split[2]), int(split[5])
        letter = password[pos1]
        password.remove(letter)
        password.insert(pos2, letter)

print("".join(password))

solution = "fbgdceah"

for j in itertools.permutations("abcdefgh"):
    password = deque(j)
    for command in commands:
        split = command.split(" ")
        if split[0] == "swap" and split[1] == "position":
            pos1, pos2 = int(split[2]), int(split[5])
            x, y = password[pos1], password[pos2]
            password[pos1] = y
            password[pos2] = x
        if split[0] == "swap" and split[1] == "letter":
            let1, let2 = split[2], split[5]
            pos1, pos2 = password.index(let1), password.index(let2)
            password[pos1] = let2
            password[pos2] = let1
        if split[0] == "rotate" and split[1] == "right":
            steps = int(split[2])
            password.rotate(steps)
        if split[0] == "rotate" and split[1] == "left":
            steps = -int(split[2])
            password.rotate(steps)
        if split[0] == "rotate" and split[1] == "based":
            let1 = split[6]
            index = password.index(let1)
            password.rotate(1)
            password.rotate(index)
            if index > 3: password.rotate(1)
        if split[0] == "reverse":
            start, end = int(split[2]), int(split[4])
            toReplace = []
            for i in range(end, start-1, -1):
                toReplace.append(password[i])
            for i in range(start, end+1):
                password[i] = toReplace[i - start]
        if split[0] == "move":
            pos1, pos2 = int(split[2]), int(split[5])
            letter = password[pos1]
            password.remove(letter)
            password.insert(pos2, letter)
    if "".join(password) == solution: 
        print("".join(j))
        break
