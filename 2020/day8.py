with open("day8input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

for nop in range(len(lines)):
    new_lines = lines.copy()
    if "nop" in new_lines[nop]:
        new_lines[nop] = new_lines[nop].replace("nop", "jmp")
    elif "jmp" in new_lines[nop]:
        new_lines[nop] = new_lines[nop].replace("jmp", "nop")
    else:
        continue
    acc = 0
    pos = 0
    visited_pos = [0]
    while True:
        command = new_lines[pos].split(" ")
        if command[0] == "acc":
            acc += int(command[1][1:]) if command[1][0] == "+" else -int(command[1][1:])
            pos += 1
        elif command[0] == "jmp":
            jump = int(command[1][1:]) if command[1][0] == "+" else -int(command[1][1:])
            pos += jump
        elif command[0] == "nop":
            pos += 1
        if pos >= len(new_lines):
            print(acc)
            break
        if pos not in visited_pos: visited_pos.append(pos)
        else: 
            break
        if pos < 0: break

acc = 0
pos = 0
visited_pos = [0]

while True:
    command = lines[pos].split(" ")
    if command[0] == "acc":
        acc += int(command[1][1:]) if command[1][0] == "+" else -int(command[1][1:])
        pos += 1
    elif command[0] == "jmp":
        jump = int(command[1][1:]) if command[1][0] == "+" else -int(command[1][1:])
        pos += jump
    elif command[0] == "nop":
        pos += 1
    if pos not in visited_pos: visited_pos.append(pos)
    else: 
        print(acc)
        break