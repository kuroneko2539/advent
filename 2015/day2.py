import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day2Input.txt", help="file contianing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    wrappings = [[int(i) for i in x.strip().split("x")] for x in f.readlines()]

def wrappingNeeded(l,w,h):
    main = 2*l*w + 2*w*h + 2*h*l
    smallest = min([l*w, w*h, h*l])

    return main + smallest

def ribbonNeeded(l,w,h):
    sortedDims = sorted([l,w,h])
    perim = 2*sortedDims[0] + 2*sortedDims[1]
    bow = l*w*h

    return perim + bow

totalWrapping = 0
totalBow = 0
for i in wrappings:
    totalWrapping += wrappingNeeded(i[0],i[1],i[2])
    totalBow += ribbonNeeded(i[0],i[1],i[2])

print(totalWrapping, totalBow)