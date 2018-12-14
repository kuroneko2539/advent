import argparse, numpy as np, re
from collections import deque
import time

inputKey = "919901"

elf1 = 0
elf2 = 1

recipes = [3,7]
done = False

while True:
    newRecipes = str(recipes[elf1] + recipes[elf2])
    keys = []
    for i in range(len(newRecipes)):
        recipes.append(int(newRecipes[i]))
        keys.append("".join([str(x) for x in recipes[-len(str(inputKey)):]]))
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    for key in range(len(keys)):
        if keys[key] == str(inputKey):
            print(len(recipes) - len(str(inputKey)) - (len(keys) - 1 - key))
            done = True
            break
    print(len(recipes))
    if done: break