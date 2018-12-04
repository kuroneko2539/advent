import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day23input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [line.rstrip() for line in f]

registers0 = {}

for reg in [x for x in "abcd"]:
    registers0[reg] = 0

##PART 1: get result of a
pos0 = 0
part = 1
if part == 1:
    registers0["a"] = 7
if part == 2:
    registers0["a"] = 12
    ### Never use this, answer is 12! + x*y where x and y are values in commands 20 and 21

while True:
    split = commands[pos0].split(" ")
    instruction = split[0]
    arg1 = split[1]    
    if len(split) > 2:
        arg2 = split[2]
    else:
        arg2 = None
    # if str.isalpha(arg1):
    #     print(pos0, instruction, arg1, registers0[arg1])
    # else:
    #     print(pos0, instruction, arg1)
    if instruction == "cpy":
        if str.isalpha(arg1):
            registers0[arg2] = int(registers0[arg1])
        else:
            registers0[arg2] = int(arg1)
    elif instruction == "tgl":
        if str.isalpha(arg1):
            steps = int(registers0[arg1])
        else:
            steps = int(arg1)
        if pos0 + steps < 0 or pos0 + steps >= len(commands):
            pass
        else:
            split = commands[pos0 + steps].split(" ")
            instructionAtStep = split[0]
            if len(split) == 2:
                if instructionAtStep == "inc":
                    commands[pos0+steps] = "dec" + commands[pos0+steps][3:]
                else:
                    commands[pos0+steps] = "inc" + commands[pos0+steps][3:]
            else:
                if instructionAtStep == "jnz":
                    commands[pos0+steps] = "cpy" + commands[pos0+steps][3:]
                else:
                    commands[pos0+steps] = "jnz" + commands[pos0+steps][3:]
    elif instruction == "inc":
        registers0[arg1] += 1
    elif instruction == "dec":
        registers0[arg1] -= 1
    elif instruction == "jnz":
        if str.isalpha(arg1):
            if registers0[arg1] != 0:
                if str.isalpha(arg2):
                    pos0 += registers0[arg2]
                    if pos0 < 0 or pos0 > len(commands) - 1: break
                    continue
                else:
                    pos0 += int(arg2)
                    if pos0 < 0 or pos0 > len(commands) - 1: break
                    continue
        else:
            if int(arg1) != 0:
                if str.isalpha(arg2):
                    pos0 += registers0[arg2]
                    if pos0 < 0 or pos0 > len(commands) - 1: break
                    continue
                else:
                    pos0 += int(arg2)
                    if pos0 < 0 or pos0 > len(commands) - 1: break
                    continue
    else:
        print("BROKEN")
    pos0 += 1
    if pos0 < 0 or pos0 > len(commands) - 1: break

print(registers0["a"])