with open("day17input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

cubes = []
for line in range(len(lines)):
    for char in range(len(lines[line])):
        if lines[line][char] == "#":
            cubes.append([line,char,0,0])


for i in range(6):
    new_cubes = []
    xmin = min([x[0] for x in cubes]) - 1
    xmax = max([x[0] for x in cubes]) + 2
    ymin = min([x[1] for x in cubes]) - 1
    ymax = max([x[1] for x in cubes]) + 2
    zmin = min([x[2] for x in cubes]) - 1
    zmax = max([x[2] for x in cubes]) + 2
    wmin = min([x[3] for x in cubes]) - 1
    wmax = max([x[3] for x in cubes]) + 2
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            for z in range(zmin, zmax):
                for w in range(wmin, wmax):
                    surrounding_active = 0
                    is_active = 1 if [x, y, z, w] in cubes else 0
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            for k in [-1, 0, 1]:
                                for l in [-1, 0, 1]:
                                    if i == 0 and j == 0 and k == 0 and l == 0: continue
                                    if [x+i,y+j,z+k,w+l] in cubes:
                                        surrounding_active += 1
                    if surrounding_active == 3 and is_active == 0:
                        new_cubes.append([x,y,z,w])
                    if (surrounding_active == 2 or surrounding_active == 3) and is_active == 1:
                        new_cubes.append([x,y,z,w])
    cubes = new_cubes.copy()

print(len(cubes))