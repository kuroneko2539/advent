import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day18input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [line.rstrip() for line in f]

registers0 = {}
registers1 = {}

for command in commands:
    part = command.split(" ")
    registers0[part[1]] = 0
    registers1[part[1]] = 0

registers0["p"] = 0
registers1["p"] = 1

##PART 1: get first returned sound freuqency

lastSound = 0
pos = 0

queue0 = []
queue1 = []
pos0 = 0
pos1 = 1
oneSendCount = 0

zeroStillActive = True
oneStillActive = True


while True:
    while zeroStillActive:
        split = commands[pos0].split(" ")
        instruction = split[0]
        arg1 = split[1]
        if len(split) > 2:
            arg2 = split[2]
        else:
            arg2 = None

        if instruction == "snd":
            queue1.append(registers0[arg1])
        elif instruction == "set":
            if str.isalpha(arg2):
                registers0[arg1] = registers0[arg2]
            else:
                registers0[arg1] = int(arg2)
        elif instruction == "add":
            if str.isalpha(arg2):
                registers0[arg1] += registers0[arg2]
            else:
                registers0[arg1] += int(arg2)
        elif instruction == "mul":
            if str.isalpha(arg2):
                registers0[arg1] *= registers0[arg2]
            else:
                registers0[arg1] *= int(arg2)
        elif instruction == "mod":
            if str.isalpha(arg2):
                registers0[arg1] = registers0[arg1] % registers0[arg2]
            else:
                registers0[arg1] = registers0[arg1] % int(arg2)
        elif instruction == "rcv":
            if len(queue0) > 0:
                registers0[arg1] = queue0[0]
                del queue0[0]
            else:
                break
        elif instruction == "jgz":
            if str.isalpha(arg1):
                if registers0[arg1] > 0:
                    if str.isalpha(arg2):
                        pos0 += registers0[arg2]
                        continue
                    else:
                        pos0 += int(arg2)
                        continue
            else:
                if int(arg1) > 0:
                    if str.isalpha(arg2):
                        pos0 += registers0[arg2]
                        continue
                    else:
                        pos0 += int(arg2)
                        continue
        pos0 += 1
        if pos0 >= len(commands) or pos0 < 0:
            zeroStillActive = False
    while oneStillActive:
        split = commands[pos1].split(" ")
        instruction = split[0]
        arg1 = split[1]
        if len(split) > 2:
            arg2 = split[2]
        else:
            arg2 = None

        if instruction == "snd":
            queue0.append(registers1[arg1])
            oneSendCount += 1
        elif instruction == "set":
            if str.isalpha(arg2):
                registers1[arg1] = registers1[arg2]
            else:
                registers1[arg1] = int(arg2)
        elif instruction == "add":
            if str.isalpha(arg2):
                registers1[arg1] += registers1[arg2]
            else:
                registers1[arg1] += int(arg2)
        elif instruction == "mul":
            if str.isalpha(arg2):
                registers1[arg1] *= registers1[arg2]
            else:
                registers1[arg1] *= int(arg2)
        elif instruction == "mod":
            if str.isalpha(arg2):
                registers1[arg1] = registers1[arg1] % registers1[arg2]
            else:
                registers1[arg1] = registers1[arg1] % int(arg2)
        elif instruction == "rcv":
            if len(queue1) > 0:
                registers1[arg1] = queue1[0]
                del queue1[0]
            else:
                break
        elif instruction == "jgz":
            if str.isalpha(arg1):
                if registers1[arg1] > 0:
                    if str.isalpha(arg2):
                        pos1 += registers1[arg2]
                        continue
                    else:
                        pos1 += int(arg2)
                        continue
            else:
                if int(arg1) > 0:
                    if str.isalpha(arg2):
                        pos1 += registers1[arg2]
                        continue
                    else:
                        pos1 += int(arg2)
                        continue
        pos1 += 1
        if pos1 >= len(commands) or pos1 < 0:
            oneStillActive = False
    if len(queue0) == 0 and len(queue1) == 0:
        break

print(oneSendCount)