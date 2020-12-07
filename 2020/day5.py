with open("day5input.txt", "r") as f:
    seats = [x.strip() for x in f.readlines()]

seat_ids = {}

for seat in seats:
    col_min = 0
    col_max = 7
    row_min = 0
    row_max = 127
    for half in seat:
        if half == "F":
            row_max -= int(((row_max - row_min) + 1) / 2)
        if half == "B":
            row_min += int(((row_max - row_min) + 1) / 2)
        if half == "R":
            col_min += int(((col_max - col_min) + 1) / 2)
        if half == "L":
            col_max -= int(((col_max - col_min) + 1) / 2)
    seat_ids[row_max * 8 + col_max] = {
        "col": col_max,
        "row": row_max,
        "string": seat
    }

print(max(list(seat_ids.keys())))

min_row = min([x["row"] for ID, x in seat_ids.items()])
max_row = max([x["row"] for ID, x in seat_ids.items()])

print(min_row, max_row)

for r in range(min_row+1,max_row-1):
    for c in range(0,8):
        ID = r * 8 + c
        if ID not in seat_ids.keys():
            print(ID)