input_data = [x.strip() for x in open("./day3Input.txt", "r").readlines()]
part = 2

cable1 = input_data[0].split(",")
cable2 = input_data[1].split(",")

print(cable1)
print(cable2)

if part == 1:
    cable1Coords = [(0,0)]
    cable2Coords = [(0,0)]
elif part == 2:
    cable1Coords = [((0,0), 0)]
    cable2Coords = [((0,0), 0)]

def addCoords(curLoc, command, cableCoords, part):
    direction = command[0]
    distance = int(command[1:])

    if part == 1:
        for i in range(distance + 1):
            if direction == "L":
                cableCoords.append((curLoc[0] - i, curLoc[1]))
            elif direction == "R":
                cableCoords.append((curLoc[0] + i, curLoc[1]))
            elif direction == "U":
                cableCoords.append((curLoc[0], curLoc[1] + i))
            elif direction == "D":
                cableCoords.append((curLoc[0], curLoc[1] - i))
    elif part == 2:
        for i in range(distance + 1):
            if direction == "L":
                cableCoords.append(((curLoc[0][0] - i, curLoc[0][1]), curLoc[1] + i))
            elif direction == "R":
                cableCoords.append(((curLoc[0][0] + i, curLoc[0][1]), curLoc[1] + i))
            elif direction == "U":
                cableCoords.append(((curLoc[0][0], curLoc[0][1] + i), curLoc[1] + i))
            elif direction == "D":
                cableCoords.append(((curLoc[0][0], curLoc[0][1] - i), curLoc[1] + i))
    return cableCoords

for com in cable1:
    cable1Coords = addCoords(cable1Coords[-1], com, cable1Coords, part)
for com in cable2:
    cable2Coords = addCoords(cable2Coords[-1], com, cable2Coords, part)

if part == 1:
    inBoth = set(cable1Coords).intersection(cable2Coords)
    minDist = 10000000
    for coord in inBoth:
        if (coord[0] != 0 and coord[1] != 0):
            dist = abs(coord[0]) + abs(coord[1])
            if dist < minDist: minDist = dist

    print(minDist)
elif part == 2:
    minDelay = 10000000
    inBoth = set([x[0] for x in cable1Coords]).intersection([x[0] for x in cable2Coords])
    for coord in inBoth:
        if (coord[0] != 0 and coord[1] != 0):
            cable1Val = min([x[1] for x in cable1Coords if x[0] == coord])
            cable2Val = min([x[1] for x in cable2Coords if x[0] == coord])
            delay = cable1Val + cable2Val
            if delay < minDelay: minDelay = delay
    print(minDelay)