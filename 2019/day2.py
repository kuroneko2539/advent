import sys

input_data = [int(x.strip()) for x in open("./day2Input.txt", "r").readlines()[0].split(",")]
#print(input_data)
part =2

#sys.exit()

def execute_command(command, buffer):
    if command[0] == 1:
        buffer[command[3]] = buffer[command[1]] + buffer[command[2]]
    elif command[0] == 2:
        buffer[command[3]] = buffer[command[1]] * buffer[command[2]]
    return buffer

if part == 1:
    input_data[1] = 12
    input_data[2] = 2
    buffer = input_data.copy()

    i = 0
    while i < len(input_data):
        if buffer[i] == 99: break
        buffer = execute_command(buffer[i:i+4], buffer)
        i += 4

    print(buffer[0])

if part == 2:
    for a in range(100):
        for b in range(100):
            input_data[1] = a
            input_data[2] = b
            buffer = input_data.copy()

            i = 0
            while i < len(input_data):
                if buffer[i] == 99: break
                buffer = execute_command(buffer[i:i+4], buffer)
                i += 4

            if buffer[0] == 19690720:
                break
        if buffer[0] == 19690720:
            break
    print(100 * a + b)