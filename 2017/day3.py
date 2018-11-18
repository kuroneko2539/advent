inputNum = 289326

##PART 1: Find manhattan distance to centre

values = {}
values[(0,0)] = 1
#direction +X, +Y, -X, -Y
direction = 0
x, y = 0, 0
value = 1
layer = 1
while value < inputNum:
    if direction == 0:
        x += 1
        if x == layer:
            direction += 1
    elif direction == 1:
        y += 1
        if y == layer:
            direction += 1
    elif direction == 2:
        x -= 1
        if abs(x) == layer:
            direction += 1
            if direction == 4: direction = 0
    elif direction == 3:
        y -= 1
        if abs(y) == layer:
            layer += 1
            direction = 0
    value = value + 1
    values[(x,y)] = value

print(abs(x) + abs(y))

##PART 2: Sum of current surrounding area

values = {}
values[(0,0)] = 1
#direction +X, +Y, -X, -Y
direction = 0
x, y = 0, 0
value = 1
layer = 1
while value < inputNum:
    if direction == 0:
        x += 1
        if x == layer:
            direction += 1
    elif direction == 1:
        y += 1
        if y == layer:
            direction += 1
    elif direction == 2:
        x -= 1
        if abs(x) == layer:
            direction += 1
            if direction == 4: direction = 0
    elif direction == 3:
        y -= 1
        if abs(y) == layer:
            layer += 1
            direction = 0
    value = 0
    for xDiff in [-1,0,1]:
        for yDiff in [-1,0,1]:
            if xDiff == 0 and yDiff == 0: continue
            else:
                try:
                    value += values[(x+xDiff,y+yDiff)]
                except:
                    continue
    values[(x,y)] = value

print(value)