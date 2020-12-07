with open("day7input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

possible_colors = []
for line in lines:
    split = line.split("contain")
    if "shiny gold" in split[1]: 
        if split[0].split("bag")[0].strip() not in possible_colors: possible_colors.append(split[0].split("bag")[0].strip())

while True:
    current_colors = len(possible_colors)
    for line in lines:
        for color in possible_colors:
            split = line.split("contain")
            if color in split[1]: 
                if split[0].split("bag")[0].strip() not in possible_colors: possible_colors.append(split[0].split("bag")[0].strip())
    if len(possible_colors) == current_colors:
        break

print(len(possible_colors))

bag_dict = {"shiny gold": {}}
for line in lines:
    split = line.split("contain")
    if "shiny gold" in split[0]:
        for b in split[1].split(","):
            bag_dict["shiny gold"][b.split(" ")[2] + " " + b.split(" ")[3]] = int(b.split(" ")[1])
            bag_dict[b.split(" ")[2] + " " + b.split(" ")[3]] = {}

keys_this_term = list(bag_dict["shiny gold"].keys())
while True:
    tmp_list = []
    for line in lines:
        split = line.split("contain")
        for key in keys_this_term:
            if key in split[0]:
                if "no" in split[1]: continue
                for b in split[1].split(","):
                    bag_dict[key][b.split(" ")[2] + " " + b.split(" ")[3]] = int(b.split(" ")[1])
                    tmp_list.append(b.split(" ")[2] + " " + b.split(" ")[3])
                    bag_dict[b.split(" ")[2] + " " + b.split(" ")[3]] = {}
    keys_this_term = tmp_list
    if len(keys_this_term) == 0:
        break

def get_bags(key):
    if len(bag_dict[key]) == 0:
        return 0
    else:
        total_bags = 0
        for k in bag_dict[key].keys():
            total_bags += bag_dict[key][k] * get_bags(k) + bag_dict[key][k]
        return total_bags

print(get_bags("shiny gold"))
