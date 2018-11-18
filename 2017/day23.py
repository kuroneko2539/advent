import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day23input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [line.rstrip() for line in f]

registers0 = {}

for reg in [x for x in "abcdefgh"]:
    registers0[reg] = 0

##PART 1: get first returned sound freuqency

pos0 = 0
mulCount = 0
registers0["a"] = 1

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
    if instruction == "set":
        if str.isalpha(arg2):
            registers0[arg1] = int(registers0[arg2])
        else:
            registers0[arg1] = int(arg2)
    elif instruction == "sub":
        if str.isalpha(arg2):
            registers0[arg1] -= registers0[arg2]
        else:
            registers0[arg1] -= int(arg2)
    elif instruction == "mul":
        mulCount += 1
        if str.isalpha(arg2):
            registers0[arg1] *= registers0[arg2]
        else:
            registers0[arg1] *= int(arg2)
    elif instruction == "jnz":
        #if pos0 == 19:
            #registers0["g"] = 0
            #registers0["e"] = 106700
        if pos0 == 23:
            registers0["g"] = 0
            registers0["d"] = 106700
        if pos0 == 28:
            print(registers0)
            #registers0["g"] = 0
            #registers0["b"] = 123700
        if str.isalpha(arg1):
            if registers0[arg1] != 0:
                if str.isalpha(arg2):
                    pos0 += registers0[arg2]
                    continue
                else:
                    pos0 += int(arg2)
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
    pos0 += 1
    if pos0 < 0 or pos0 > len(commands) - 1: break

print(mulCount)
print(registers0["h"])