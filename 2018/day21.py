import argparse, numpy as np, re, sys
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day21Input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

instrReg = 4

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

registers = [0,0,0,0,0,0]

numExec = 0
instructionPointer = 0
statesSeen = []
startLoop = 0
inReg1 = []

while instructionPointer > -1 and instructionPointer < len(commands):
    #if ",".join([str(r) for r in registers]) + commands[instructionPointer] in statesSeen:
        #print("infinite")
        #break
    #else:
        #statesSeen.append(",".join([str(r) for r in registers]) + commands[instructionPointer])
        #print(statesSeen[-1])
    command = commands[instructionPointer]
    if registers[1] not in inReg1 and instructionPointer == 28:
        print(numExec, registers[1])
        inReg1.append(registers[1])       
    registers[instrReg] = instructionPointer
    split = command.split(" ")
    split[1] = int(split[1])
    split[2] = int(split[2])
    split[3] = int(split[3])
    registers = locals()[split[0]](registers, split)
    instructionPointer = registers[instrReg] + 1
    numExec += 1