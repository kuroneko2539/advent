with open("day2input.txt", "r") as f:
    passwords = [x.strip() for x in f.readlines()]

valid_count = 0
for p in passwords:
    split = p.split(" ")
    password = split[-1]
    min_count = int(split[0].split("-")[0])
    max_count = int(split[0].split("-")[1])

    count = password.count(split[1][0])
    if count >= min_count and count <= max_count:
        valid_count += 1

print(valid_count)

valid_count = 0
for p in passwords:
    split = p.split(" ")
    password = split[-1]
    pos_1 = int(split[0].split("-")[0]) - 1
    pos_2 = int(split[0].split("-")[1]) - 1
    character = split[1][0]

    if (password[pos_1] == character and password[pos_2] != character) or (password[pos_1] != character and password[pos_2] == character):
        valid_count += 1
    
print(valid_count)