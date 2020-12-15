with open("day14input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

def numberTo36Bin(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return "{:036d}".format(int("".join(digits[::-1])))

mem = {}

for line in lines:
    if "mask" in line:
        mask = line.split("=")[1].strip()
    else:
        address = line.split("[")[1].split("]")[0]
        value = numberTo36Bin(int(line.split("=")[1].strip()), 2)
        new_value = ""
        for i in range(36):
            if mask[i] == "X":
                new_value += value[i]
            else:
                new_value += mask[i]
        mem[address] = int(new_value, 2)

total = 0
for k, i in mem.items():
    total += i

print(total)

new_mem = {}

for line in lines:
    if "mask" in line:
        mask = line.split("=")[1].strip()
    else:
        address = numberTo36Bin(int(line.split("[")[1].split("]")[0]), 2)
        value = int(line.split("=")[1].strip())
        possible_addresses = [""]
        for i in range(36):
            if mask[i] == "X":
                new_ads = []
                for ad in range(len(possible_addresses)):
                    new_ads.append(possible_addresses[ad] + "1")
                    possible_addresses[ad] += "0"
                possible_addresses += new_ads
            elif mask[i] == "0":
                for ad in range(len(possible_addresses)):
                    possible_addresses[ad] += address[i]
            else:
                for ad in range(len(possible_addresses)):
                    possible_addresses[ad] += "1"
        for ad in possible_addresses:
            new_mem[ad] = value

total = 0
for k, i in new_mem.items():
    total += i

print(total)