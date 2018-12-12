import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day1Input.txt", help="file contianing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inString = [x.strip() for x in f.readlines()][0]

currentFloor = 0
beenToBasement = False
for i in range(len(inString)):
    if inString[i] == "(": currentFloor += 1
    else: currentFloor -= 1
    if currentFloor < 0 and not beenToBasement: 
        print(i+1)
        beenToBasement = True


print(currentFloor)