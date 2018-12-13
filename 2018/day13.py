import argparse, numpy as np, re
import matplotlib.pyplot as plt
import time

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day13input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    rows = [x for x in f.readlines()]

## grid pos: 0 = Empty, 1 = -, 2 = |, 3 = +, 4 = \, 5 = /
## dir: 0 = ^, 1 = >, 2 = v, 3 = <
## turn: -1 = <, 0 = ^, 1 = >

grid = np.zeros((len(rows),len(rows[0])))
gridCarts = np.zeros((len(rows),len(rows[0])))
carts = {}
cartCount = 1

for row in range(len(rows)):
    for col in range(len(rows[row])):
        if rows[row][col] == " ":
            grid[row,col] = 0
        elif rows[row][col] == "-":
            grid[row,col] = 1
        elif rows[row][col] == "|":
            grid[row,col] = 2
        elif rows[row][col] == "+":
            grid[row,col] = 3
        elif rows[row][col] == "\\":
            grid[row,col] = 4
        elif rows[row][col] == "/":
            grid[row,col] = 5
        elif rows[row][col] == "^":
            grid[row,col] = 2
            gridCarts[row,col] = cartCount
            carts[cartCount] = {"row": row, "col": col, "dir": 0, "turn": -1}
            cartCount += 1
        elif rows[row][col] == "v":
            grid[row,col] = 2
            gridCarts[row,col] = cartCount
            carts[cartCount] = {"row": row, "col": col, "dir": 2, "turn": -1}
            cartCount += 1
        elif rows[row][col] == ">":
            grid[row,col] = 2
            gridCarts[row,col] = cartCount
            carts[cartCount] = {"row": row, "col": col, "dir": 1, "turn": -1}
            cartCount += 1
        elif rows[row][col] == "<":
            grid[row,col] = 2
            gridCarts[row,col] = cartCount
            carts[cartCount] = {"row": row, "col": col, "dir": 3, "turn": -1}
            cartCount += 1

done = False
part = 2
while True:
    cartsMoved = []
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if gridCarts[i,j] > 0 and gridCarts[i,j] not in cartsMoved:
                cart = int(gridCarts[i,j])
                cartsMoved.append(cart)
            else: continue
            
            gridCarts[carts[cart]["row"],carts[cart]["col"]] -= cart
            if carts[cart]["dir"] == 0:
                carts[cart]["row"] -= 1
            elif carts[cart]["dir"] == 2:
                carts[cart]["row"] += 1
            elif carts[cart]["dir"] == 1:
                carts[cart]["col"] += 1
            elif carts[cart]["dir"] == 3:
                carts[cart]["col"] -= 1
            if gridCarts[carts[cart]["row"],carts[cart]["col"]] > 0 and part == 1:
                print(carts[cart]["col"],carts[cart]["row"])
                done = True
                break
            elif gridCarts[carts[cart]["row"],carts[cart]["col"]] > 0 and part == 2:
                cart2 = gridCarts[carts[cart]["row"],carts[cart]["col"]]
                gridCarts[carts[cart]["row"],carts[cart]["col"]] = 0
                del carts[cart]
                del carts[cart2]
                continue
            else:
                gridCarts[carts[cart]["row"],carts[cart]["col"]] += cart

            if grid[carts[cart]["row"],carts[cart]["col"]] == 3:
                carts[cart]["dir"] += carts[cart]["turn"]
                if carts[cart]["dir"] == -1: carts[cart]["dir"] = 3
                if carts[cart]["dir"] == 4: carts[cart]["dir"] = 0
                carts[cart]["turn"] += 1
                if carts[cart]["turn"] > 1: carts[cart]["turn"] = -1
            elif grid[carts[cart]["row"],carts[cart]["col"]] == 5:
                if carts[cart]["dir"] == 0: carts[cart]["dir"] = 1
                elif carts[cart]["dir"] == 2: carts[cart]["dir"] = 3
                elif carts[cart]["dir"] == 1: carts[cart]["dir"] = 0
                elif carts[cart]["dir"] == 3: carts[cart]["dir"] = 2
            elif grid[carts[cart]["row"],carts[cart]["col"]] == 4:
                if carts[cart]["dir"] == 0: carts[cart]["dir"] = 3
                elif carts[cart]["dir"] == 2: carts[cart]["dir"] = 1
                elif carts[cart]["dir"] == 1: carts[cart]["dir"] = 2
                elif carts[cart]["dir"] == 3: carts[cart]["dir"] = 0
        if done: break
    if done: break
    if len(carts) == 1:
        print(carts)
        break
    else:
        print(len(carts))