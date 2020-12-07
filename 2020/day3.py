with open("day3input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
total = 1
for slope in slopes:
    pos = [0,0]
    treecount = 0
    while pos[1] < len(lines) -1:
        pos[1] += slope[1]
        pos[0] = (pos[0] + slope[0]) % len(lines[0])
        if lines[pos[1]][pos[0]] == "#": treecount += 1
    total *= treecount

print(total)
