tape = {}

position = 0
tape[position] = 0

state = "A"

for _ in range(12134527):
    currentValue = tape[position]

    if state == "A":
        if currentValue == 0:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "B"
        else:
            tape[position] = 0
            position -= 1
            if position not in tape.keys():
                tape[position] = 0
            state = "C"

    elif state == "B":
        if currentValue == 0:
            tape[position] = 1
            position -= 1
            if position not in tape.keys():
                tape[position] = 0
            state = "A"
        else:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "C"

    elif state == "C":
        if currentValue == 0:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "A"
        else:
            tape[position] = 0
            position -= 1
            if position not in tape.keys():
                tape[position] = 0
            state = "D"

    elif state == "D":
        if currentValue == 0:
            tape[position] = 1
            position -= 1
            if position not in tape.keys():
                tape[position] = 0
            state = "E"
        else:
            tape[position] = 1
            position -= 1
            if position not in tape.keys():
                tape[position] = 0
            state = "C"

    elif state == "E":
        if currentValue == 0:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "F"
        else:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "A"

    elif state == "F":
        if currentValue == 0:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "A"
        else:
            tape[position] = 1
            position += 1
            if position not in tape.keys():
                tape[position] = 0
            state = "E"

print(sum(tape.values()))
