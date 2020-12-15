with open("day15input.txt", "r") as f:
    sequence = [int(x.strip()) for x in f.readlines()[0].split(",")]


most_recent_indices = {x: [sequence.index(x)] for x in sequence}
last_num = sequence[-1]
count = len(sequence)
while count < 30000000:
    if len(most_recent_indices[last_num]) >= 2:
        current_num = most_recent_indices[last_num][-1] - most_recent_indices[last_num][-2]
    else:
        current_num = 0
    if current_num not in most_recent_indices:
        most_recent_indices[current_num] = []
    most_recent_indices[current_num].append(count)
    last_num = current_num
    count += 1

print(last_num)
