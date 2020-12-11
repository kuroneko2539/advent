import numpy as np

with open("day11input.txt", "r") as f:
    grid = [x.strip() for x in f.readlines()]
checks = [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,-1],
        [0,1],
        [1,-1],
        [1,0],
        [1,1]
    ]
iterations = 0
while True:
    new_grid = []
    changes = 0
    for i in range(len(grid)):
        new_line = []
        for j in range(len(grid[0])):
            current = grid[i][j]
            occupied = 0
            for check in checks:
                icheck = i + check[0]
                if icheck < 0 or icheck == len(grid): continue
                jcheck = j + check[1]
                if jcheck < 0 or jcheck == len(grid[0]): continue
                if grid[icheck][jcheck] == "#": occupied += 1
            if current == "L" and occupied == 0:
                new_line.append("#")
                changes += 1
            elif current == "#" and occupied >= 4:
                new_line.append("L")
                changes += 1
            else:
                new_line.append(current)
        new_grid.append(new_line)
    grid = new_grid.copy()
    iterations += 1
    if changes == 0:
        print(iterations)
        print(sum([x.count("#") for x in grid]))
        break

with open("day11input.txt", "r") as f:
    grid = [x.strip() for x in f.readlines()]
checks = [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,-1],
        [0,1],
        [1,-1],
        [1,0],
        [1,1]
    ]
closest_visibles = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        closest_visibles[(i,j)] = [] 
        for check in checks:
            checker = "0"
            icheck = i
            jcheck = j
            found = True
            while checker != "L" and checker != "#":
                icheck += check[0]
                if icheck < 0 or icheck == len(grid): 
                    found = False
                    break
                jcheck += check[1]
                if jcheck < 0 or jcheck == len(grid[0]): 
                    found = False
                    break
                checker = grid[icheck][jcheck]
            if found: closest_visibles[(i,j)].append((icheck,jcheck))
iterations = 0
while True:
    new_grid = []
    changes = 0
    for i in range(len(grid)):
        new_line = []
        for j in range(len(grid[0])):
            current = grid[i][j]
            occupied = 0
            for vis in closest_visibles[(i,j)]:
                if grid[vis[0]][vis[1]] == "#": occupied += 1
            if current == "L" and occupied == 0:
                new_line.append("#")
                changes += 1
            elif current == "#" and occupied >= 5:
                new_line.append("L")
                changes += 1
            else:
                new_line.append(current)
        new_grid.append(new_line)
    grid = new_grid.copy()
    iterations += 1
    if changes == 0:
        print(iterations)
        print(sum([x.count("#") for x in grid]))
        break