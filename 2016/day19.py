numberOfElves = 3012210

part1 = False
part2 = True

if part1:
    elves = {}
    for i in range(numberOfElves):
        elves[i] = 1

    numberOfElvesRemoved = 0

    while numberOfElvesRemoved < numberOfElves - 1:
        print(numberOfElvesRemoved)
        for i in range(numberOfElves):
            if elves[i] != 0:
                k = 1
                while elves[(i+k) % numberOfElves] == 0: k += 1
                if elves[(i+k) % numberOfElves] != 0:
                    elves[i] += elves[(i+k) % numberOfElves]
                    elves[(i+k) % numberOfElves] = 0
                    numberOfElvesRemoved += 1
                    if numberOfElvesRemoved == numberOfElves - 1: 
                        print()
                        print(i+1) 
                        break

if part2:
    elves = []
    for i in range(numberOfElves):
        elves.append({"ID": i+1, "numPres": 1})

    numberOfElvesRemoved = 0

    pos = 0
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            checkAt = (pos + int(len(elves) / 2)) % len(elves)
        else:
            checkAt = (pos + int((len(elves) - 1) / 2)) % len(elves)
        elves[pos]["numPres"] += elves[checkAt]["numPres"]
        del elves[checkAt]
        pos = (pos + 1) % len(elves)
    print(elves[0]["ID"])
