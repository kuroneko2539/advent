import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day6input.txt", help="file containing input key")
args = parser.parse_args()

##PART 1: how many steps to reach same state when redistributing from step 0

with open(args.inFile, "r") as f:
    banks = [int(x) for x in f.readlines()[0].split("\t")]

previousStates = []
steps = 0
while True:
    previousStates.append(banks.copy())
    steps += 1
    bankToRedist = np.argmax(banks)
    current = bankToRedist + 1
    elements = banks[bankToRedist]
    banks[bankToRedist] = 0
    for _ in range(elements):
        if current == len(banks): current = 0
        banks[current] += 1
        current += 1
    done = False
    for state in previousStates:
        if banks == state: 
            done = True
            break
    if done: break
print(steps)

##PART 2: how many steps in loop to reach the repeated state

with open(args.inFile, "r") as f:
    banks = [int(x) for x in f.readlines()[0].split("\t")]

previousStates = []
steps = 0
while True:
    previousStates.append(banks.copy())
    steps += 1
    bankToRedist = np.argmax(banks)
    current = bankToRedist + 1
    elements = banks[bankToRedist]
    banks[bankToRedist] = 0
    for _ in range(elements):
        if current == len(banks): current = 0
        banks[current] += 1
        current += 1
    done = False
    for state in range(len(previousStates)):
        if banks == previousStates[state]: 
            done = True
            numInLoop = steps - state
            break
    if done: break
print(numInLoop)