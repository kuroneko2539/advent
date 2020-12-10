with open("day10input.txt", "r") as f:
    jolts = [int(x.strip()) for x in f.readlines()]

jolts.append(0)
jolts = sorted(jolts)
jolts.append(jolts[-1] + 3)

ones, twos, threes = [], [], []
for j in range(1,len(jolts)):
    diff = jolts[j] - jolts[j - 1]
    if diff == 1: ones.append(1)
    if diff == 2: twos.append(1)
    if diff == 3: threes.append(1)

combos = {j: 0 for j in jolts}
combos[0] = 1

for j in jolts[1:]:
    if j-1 in combos:
        combos[j] += combos[j-1]
    if j-2 in combos:
        combos[j] += combos[j-2]
    if j-3 in combos:
        combos[j] += combos[j-3]

print(combos[jolts[-1]])