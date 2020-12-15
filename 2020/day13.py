from itertools import count
with open("day13input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]
    earliest_dept = int(lines[0])
    buses = [int(x)  if x != "x" else "x" for x in lines[1].split(",")]

lowest_wait = 100000000
best_bus = None
for bus in buses:
    if bus == "x": continue
    wait = bus - (earliest_dept % bus)
    if wait < lowest_wait:
        lowest_wait = wait
        best_bus = bus
    
print(best_bus, lowest_wait, best_bus*lowest_wait)

bus_indices = [(x, buses.index(x)) for x in buses if x != "x"]

lcm = 1
duration = 0    
for i in range(len(bus_indices)-1):
	bus_id = bus_indices[i+1][0]
	value = bus_indices[i+1][1]
	lcm *= bus_indices[i][0]
	while (duration + value) % bus_id != 0:
		duration += lcm
        
print(duration)