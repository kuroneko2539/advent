steps = 328

buffer = [0]
val = 1
pos = 0

for _ in range(2017):
    pos = (pos + steps) % len(buffer)
    buffer.insert(pos + 1, val)
    val = val + 1
    pos = pos + 1

print(buffer[pos + 1])

valAtOne = None
pos = 0
val = 1

for length in range(50000000):
    pos = (pos + steps) % (length + 1)
    if pos == 0: valAtOne = val
    val += 1
    pos += 1

print(valAtOne)