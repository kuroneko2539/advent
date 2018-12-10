import argparse, re, string, sys

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day8input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]
    numbers = [int(x) for x in commands[0].split(" ")]

def getNode(data):
    numChildren, metadata = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(numChildren):
        total, score, data = getNode(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metadata])

    if numChildren == 0:
        return totals, sum(data[:metadata]), data[metadata:]
    else:
        return (otals,sum(scores[k - 1] for k in data[:metadata] if k > 0 and k <= len(scores)),data[metadata:]

total, value, toGo = getNode(numbers)

print(total)
print(value)
