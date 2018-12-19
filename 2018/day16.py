import argparse, numpy as np, re

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day16input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

part1Commands = commands[:3119]
part2Commands = commands[3122:]

def addr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] + registers[operation[2]]
    registers[operation[3]] = result

    return registers

def addi(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] + operation[2]
    registers[operation[3]] = result

    return registers

def mulr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] * registers[operation[2]]
    registers[operation[3]] = result

    return registers

def muli(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] * operation[2]
    registers[operation[3]] = result

    return registers

def banr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] & registers[operation[2]]
    registers[operation[3]] = result

    return registers

def bani(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] & operation[2]
    registers[operation[3]] = result

    return registers

def borr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] | registers[operation[2]]
    registers[operation[3]] = result

    return registers

def bori(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] | operation[2]
    registers[operation[3]] = result

    return registers

def setr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]]
    registers[operation[3]] = result

    return registers

def seti(registers, operation):
    registers = registers.copy()
    result = operation[1]
    registers[operation[3]] = result

    return registers

def gtir(registers, operation):
    registers = registers.copy()
    result = operation[1] > registers[operation[2]]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

def gtri(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] > operation[2]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

def gtrr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] > registers[operation[2]]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

def eqir(registers, operation):
    registers = registers.copy()
    result = operation[1] == registers[operation[2]]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

def eqri(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] == operation[2]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

def eqrr(registers, operation):
    registers = registers.copy()
    result = registers[operation[1]] == registers[operation[2]]
    if result: registers[operation[3]] = 1
    else: registers[operation[3]] = 0

    return registers

greaterThanTwo = 0
opCodes = {}
for i in range(16):
    opCodes[i] = []
for i in range(0,len(part1Commands),4):
    initialReg = [int(x) for x in re.findall("\[(.*?)\]", part1Commands[i])[0].split(",")]
    operation = [int(x.strip()) for x in part1Commands[i+1].split(" ")]
    endReg = [int(x) for x in re.findall("\[(.*?)\]", part1Commands[i+2])[0].split(",")]

    opCount = 0
    if addr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("addr")
        opCount += 1
    if addi(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("addi")
        opCount += 1
    if mulr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("mulr")
        opCount += 1
    if muli(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("muli")
        opCount += 1
    if banr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("banr")
        opCount += 1
    if bani(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("bani")
        opCount += 1
    if borr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("borr")
        opCount += 1
    if bori(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("bori")
        opCount += 1
    if setr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("setr")
        opCount += 1
    if seti(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("seti")
        opCount += 1
    if gtir(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("gtir")
        opCount += 1
    if gtri(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("gtri")
        opCount += 1
    if gtrr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("gtrr")
        opCount += 1
    if eqir(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("eqir")
        opCount += 1
    if eqri(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("eqri")
        opCount += 1
    if eqrr(initialReg, operation) == endReg: 
        opCodes[operation[0]].append("eqrr")
        opCount += 1
    if opCount > 2: greaterThanTwo += 1
    
print(greaterThanTwo)
setOpCodes = {}
while len(setOpCodes) < 16:
    for i in range(16):
        if i in setOpCodes.keys(): continue
        if len(opCodes[i]) == 0:
            setOpCodes[i] = None
            continue
        if opCodes[i].count(opCodes[i][0]) == len(opCodes[i]):
            operation = opCodes[i][0]
            setOpCodes[i] = operation
            for j in range(16):
                if j in setOpCodes.keys(): continue
                opCodes[j] = [x for x in opCodes[j] if x != operation]

print(setOpCodes)

reg = [0,0,0,0]
for oper in part2Commands:
    op = [int(x) for x in oper.split(" ")]
    reg = locals()[setOpCodes[op[0]]](reg, op)
print(reg)