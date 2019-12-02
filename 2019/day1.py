input_data = [int(x.strip()) for x in open("./day1Input.txt", "r").readlines()]
part = 2

def fuel(mass, part):
    if part == 1:
        return int(mass/3.0) - 2
    elif part == 2:
        fuel_tot = int(mass/3.0) - 2
        if fuel_tot < 0:
            return 0
        fuel_tot += fuel(fuel_tot, 2)
        return fuel_tot
    

total_fuel = 0
for mass in input_data:
    total_fuel += fuel(mass, part)

print(open("./day1Input.txt", "r").readlines())
print(total_fuel)