import argparse, numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day22input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    dfLines = [x.strip() for x in f.readlines()]

df = pd.read_table(args.inFile, skiprows=1, delim_whitespace=True)
df['Used'] = df['Used'].map(lambda x: int(x.rstrip('T')))
df['Avail'] = df['Avail'].map(lambda x: int(x.rstrip('T')))
pairs = 0

for i in range(len(df)):
    nodeI = df.iloc[i]["Filesystem"]
    usedOnI = df.iloc[i]["Used"]
    availOnI = df.iloc[i]["Avail"]
    if usedOnI > 0:
        if availOnI > usedOnI:
            pairs += len(df[df["Avail"] > usedOnI]) - 1
        else:
            pairs += len(df[df["Avail"] > usedOnI])

print(pairs)
## PART 2 CALC BY HAND