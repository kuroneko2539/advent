import math
with open("day12input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

pos = [0,0]
heading = [1,0]

for ins in lines:
    if ins[0] == "N":
        pos[1] += int(ins[1:])
    if ins[0] == "E":
        pos[0] += int(ins[1:])
    if ins[0] == "S":
        pos[1] -= int(ins[1:])
    if ins[0] == "W":
        pos[0] -= int(ins[1:])
    if ins[0] == "F":
        pos[0] += int(ins[1:])*heading[0]
        pos[1] += int(ins[1:])*heading[1]
    if ins[0] == "R":
        if int(ins[1:]) == 180:
            heading[0] = -heading[0]
            heading[1] = -heading[1]
        if int(ins[1:]) == 90:
            new_heading = []
            new_heading.append(int(math.cos(math.radians(90)) * heading[0] + math.sin(math.radians(90)) * heading[1]))
            new_heading.append(int(-math.sin(math.radians(90)) * heading[0] + math.cos(math.radians(90)) * heading[1]))
            heading = new_heading
        if int(ins[1:]) == 270:
            new_heading = []
            new_heading.append(int(math.cos(math.radians(90)) * heading[0] - math.sin(math.radians(90)) * heading[1]))
            new_heading.append(int(math.sin(math.radians(90)) * heading[0] + math.cos(math.radians(90)) * heading[1]))
            heading = new_heading
    if ins[0] == "L":
        if int(ins[1:]) == 180:
            heading[0] = -heading[0]
            heading[1] = -heading[1]
        if int(ins[1:]) == 90:
            new_heading = []
            new_heading.append(int(math.cos(math.radians(90)) * heading[0] - math.sin(math.radians(90)) * heading[1]))
            new_heading.append(int(math.sin(math.radians(90)) * heading[0] + math.cos(math.radians(90)) * heading[1]))
            heading = new_heading
        if int(ins[1:]) == 270:
            new_heading = []
            new_heading.append(int(math.cos(math.radians(90)) * heading[0] + math.sin(math.radians(90)) * heading[1]))
            new_heading.append(int(-math.sin(math.radians(90)) * heading[0] + math.cos(math.radians(90)) * heading[1]))
            heading = new_heading

print(abs(pos[0]) + abs(pos[1]))

pos = [0, 0]
waypoint = [10, 1]

for ins in lines:
    if ins[0] == "N":
        waypoint[1] += int(ins[1:])
    if ins[0] == "E":
        waypoint[0] += int(ins[1:])
    if ins[0] == "S":
        waypoint[1] -= int(ins[1:])
    if ins[0] == "W":
        waypoint[0] -= int(ins[1:])
    if ins[0] == "F":
        diff0 = (waypoint[0] - pos[0])
        diff1 = (waypoint[1] - pos[1])
        pos[0] += int(ins[1:])*diff0
        pos[1] += int(ins[1:])*diff1
        waypoint[0] += int(ins[1:])*diff0
        waypoint[1] += int(ins[1:])*diff1
    if ins[0] == "L" or ins[0] == "R":
        rel_waypoint = []
        rel_waypoint.append(waypoint[0] - pos[0])
        rel_waypoint.append(waypoint[1] - pos[1])
        angle = int(ins[1:])
        if ins[0] == "R": angle = -angle
        new_relwaypoint = []
        new_relwaypoint.append(int(round(math.cos(math.radians(angle)) * rel_waypoint[0] - math.sin(math.radians(angle)) * rel_waypoint[1])))
        new_relwaypoint.append(int(round(math.sin(math.radians(angle)) * rel_waypoint[0] + math.cos(math.radians(angle)) * rel_waypoint[1])))
        waypoint[0] = pos[0] + new_relwaypoint[0]
        waypoint[1] = pos[1] + new_relwaypoint[1]

print(abs(pos[0]) + abs(pos[1]))