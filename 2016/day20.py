import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day20input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    blockedList = [x.strip() for x in f.readlines()]

blockedStarts, blockedEnds = [], []

for block in blockedList:
    blockedStarts.append(int(block.split("-")[0]))
    blockedEnds.append(int(block.split("-")[1]))

blockedStarts = sorted(blockedStarts)
blockedEnds = sorted(blockedEnds)