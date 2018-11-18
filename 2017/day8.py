import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day8input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [line.rstrip() for line in f]

registers = {}

for command in commands:
    part = command.split(" ")
    registers[part[0]] = 0
    registers[part[4]] = 0

##PART 1&2: find maximum value of any register

maxVal = 0

for command in commands:
    part = command.split(" ")
    toCompare = part[4]
    compare = part[5]
    withCompare = int(part[6])

    toModify = part[0]
    byMethod = part[1]
    byAmount = int(part[2])

    modify = False
    if compare == ">":
        if registers[toCompare] > withCompare:
            modify = True
    if compare == "<":
        if registers[toCompare] < withCompare:
            modify = True
    if compare == ">=":
        if registers[toCompare] >= withCompare:
            modify = True
    if compare == "==":
        if registers[toCompare] == withCompare:
            modify = True
    if compare == "<=":
        if registers[toCompare] <= withCompare:
            modify = True
    if compare == "!=":
        if registers[toCompare] != withCompare:
            modify = True

    if modify:
        if byMethod == "inc":
            registers[toModify] += byAmount
            if registers[toModify] > maxVal: maxVal = registers[toModify]
        if byMethod == "dec":
            registers[toModify] -= byAmount
            if registers[toModify] > maxVal: maxVal = registers[toModify]

print(max(registers.values()))
print(maxVal)