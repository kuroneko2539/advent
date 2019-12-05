import sys

input_data = [int(x.strip()) for x in open("./day5Input.txt", "r").readlines()[0].split(",")]
#print(input_data)
part = 2

outputsList = []
if part == 1:
    inVal = 1   
else:
    inVal = 5

#sys.exit()

def getCommand(buffer, position):
    fullCommand = "{:05d}".format(buffer[position])
    opcode = int(fullCommand[-2:])
    paramMode1 = int(fullCommand[-3])
    paramMode2 = int(fullCommand[-4])
    paramMode3 = int(fullCommand[-5])

    return (opcode, paramMode1, paramMode2, paramMode3)

def executeCommand(buffer, command, position):
    global outputsList, inVal
    if command[0] == 1:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        buffer[buffer[position+3]] = a + b
        position = position + 4
    elif command[0] == 2:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        buffer[buffer[position+3]] = a * b
        position = position + 4      
    elif command[0] == 3:
        buffer[buffer[position+1]] = inVal
        position = position + 2
    elif command[0] == 4:
        if command[1] == 0:
            outputsList.append(buffer[buffer[position+1]])
        else:
            outputsList.append(buffer[position+1])
        position = position + 2
    elif command[0] == 5:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        if a != 0:
            position = b
        else:
            position = position + 3
    elif command[0] == 6:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        if a == 0:
            position = b
        else:
            position = position + 3
    elif command[0] == 7:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        if a < b:
            buffer[buffer[position+3]] = 1
        else:
            buffer[buffer[position+3]] = 0
        position = position + 4
    elif command[0] == 8:
        if command[1] == 0:
            a = buffer[buffer[position+1]]
        else:
            a = buffer[position+1]
        if command[2] == 0:
            b = buffer[buffer[position+2]]
        else:
            b = buffer[position+2]
        if a == b:
            buffer[buffer[position+3]] = 1
        else:
            buffer[buffer[position+3]] = 0
        position = position + 4
    else:
        return buffer, None
    return buffer, position

position = 0
buffer = input_data
while position is not None:
    command = getCommand(buffer, position)
    print(position, command)
    print(buffer[position:position+4])
    buffer, position = executeCommand(buffer, command, position)

print(outputsList[-1])