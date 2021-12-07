depths = [int(x.strip()) for x in open("day1.txt", "r").readlines()]

increases = 0
for i in range(1,len(depths)):
    if depths[i] > depths[i-1]: increases += 1
print(increases)

increases = 0
for i in range(3, len(depths)):
    d1 = depths[i-3] + depths[i-2] + depths[i-1]
    d2 = depths[i-2] + depths[i-1] + depths[i]
    if d2 > d1: increases += 1
print(increases)