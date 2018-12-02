import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day2input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    boxes = [x.strip() for x in f.readlines()]

twoCount = 0
threeCount = 0
for box in boxes:
    for c in box:
        if box.count(c) == 2:
            twoCount += 1
            break
    for c in box:
        if box.count(c) == 3:
            threeCount += 1
            break

print(twoCount * threeCount)

exitLoop = False
finalAnswer = ""
for box in boxes:
    for box2 in boxes:
        diffCount = 0
        for i in range(len(box)):
            if box[i] != box2[i]:
                diffCount += 1
        if diffCount == 1:
            exitLoop = True
            for i in range(len(box)):
                if box[i] == box2[i]:
                    finalAnswer += box[i]
        if exitLoop: break
    if exitLoop: break

print(finalAnswer)