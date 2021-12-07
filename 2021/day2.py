instructions = [["x" if x.strip().split(" ")[0] == "forward" else "z", int(x.strip().split(" ")[1]) if x.strip().split(" ")[0] == "forward" or x.strip().split(" ")[0] == "down" else -int(x.strip().split(" ")[1])] for x in open("day2.txt", "r").readlines()]

x, z = 0, 0

for ins in instructions:
    if ins[0] == "x":
        x += ins[1]
    else:
        z += ins[1]

print(x*z)

x, z, aim = 0, 0, 0
for ins in instructions:
    if ins[0] == "x":
        x += ins[1]
        z += ins[1] * aim
    else:
        aim += ins[1]

print(x*z)