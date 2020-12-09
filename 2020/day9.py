with open("day9input.txt", "r") as f:
    lines = [int(x.strip()) for x in f.readlines()]

for i in range(25, len(lines)):
    possible_values = []
    for x in range(0,25):
        for y in range(x,25):
            possible_values.append(lines[i-x-1]+lines[i-y-1])
    if lines[i] not in possible_values:
        value = lines[i]
        print(value)
        break

for i in range(len(lines)):
    curr = 0
    mini = 0
    maxi = 1e15
    pos = i
    while curr < value:
        curr += lines[pos]
        if lines[pos] > mini:
            mini = lines[pos]
        if lines[pos] < maxi:
            maxi = lines[pos]
        pos += 1
    if curr == value:
        print(mini + maxi)
