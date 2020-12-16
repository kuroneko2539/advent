with open("day16input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

valid_values = []
class_restrictions = {}
class_map = {}
for i in range(20):
    line = lines[i]
    first = line.split(":")[1].split("or")[0].strip()
    second = line.split(":")[1].split("or")[1].strip()
    valid_values += list(range(int(first.split("-")[0]),int(first.split("-")[1])+1))
    valid_values += list(range(int(second.split("-")[0]),int(second.split("-")[1])+1))
    class_restrictions[line.split(":")[0]] = list(range(int(first.split("-")[0]),int(first.split("-")[1])+1)) + list(range(int(second.split("-")[0]),int(second.split("-")[1])+1))
    class_map[line.split(":")[0]] = []

invalid_values = []
valid_tickets = []
for i in range(25,266):
    invalid = False
    values = [int(x) for x in lines[i].split(",")]
    for value in values:
        if value not in valid_values:
            invalid_values.append(value)
            invalid = True
    if not invalid:
        valid_tickets.append(values)
values = [int(x) for x in lines[22].split(",")]
valid_tickets.append(values)

print(sum(invalid_values))

for i in range(20):
    poss_values = [x[i] for x in valid_tickets]
    for k, allowed in class_restrictions.items():
        matched = True
        for value in poss_values:
            if value not in allowed:
                if k == "zone": print(value)
                matched = False
                break
        if matched:
            class_map[k].append(i)

with open("test.csv", "w") as f:
    for k, i in class_map.items():
        f.write("{},".format(k))
        for c in range(20):
            if c in i:
                f.write("{},".format(c))
            else:
                f.write(",")
        f.write("\n")

print(valid_tickets[-1])
multi = valid_tickets[-1][4]*valid_tickets[-1][5]*valid_tickets[-1][6]*valid_tickets[-1][15]*valid_tickets[-1][17]*valid_tickets[-1][18]
print(multi)