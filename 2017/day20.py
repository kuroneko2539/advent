import argparse
from operator import add
import pandas as pd
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day20input.txt", help="file containing input key")
args = parser.parse_args()

particles = []
with open(args.inFile, "r") as f:
    particleIns = [line.rstrip() for line in f]
    for i in range(len(particleIns)):
        string = particleIns[i]
        pos = [int(x) for x in string.split("p=<")[1].split(">")[0].split(",")]
        vel = [int(x) for x in string.split("v=<")[1].split(">")[0].split(",")]
        acc = [int(x) for x in string.split("a=<")[1].split(">")[0].split(",")]
        particles.append({"ID": i, "p": pos, "v": vel, "a": acc, "distance": sum([abs(x) for x in pos]), "decreasing": True})

lowestAccel = 1
lowestAccelParts = []
for particle in particles:
    if sum([abs(x) for x in particle["a"]]) == lowestAccel: 
        lowestAccelParts.append(particle)

lowestVel = 125
lowestVelParts = []
for particle in lowestAccelParts:
    if sum([abs(x) for x in particle["v"]]) == lowestVel: 
        lowestVelParts.append(particle)

print(lowestVelParts)

for particle in particles:
    particle["pX"] = particle["p"][0]
    particle["pY"] = particle["p"][1]
    particle["pZ"] = particle["p"][2]
    particle["vX"] = particle["v"][0]
    particle["vY"] = particle["v"][1]
    particle["vZ"] = particle["v"][2]

df = pd.DataFrame(particles)

lastVals = deque(maxlen=20)
for i in range(10000):
    df = df.drop_duplicates(subset=["pX","pY","pZ"], keep=False, inplace=False).reset_index(drop=True)
    for j in range(len(df)):
         df.ix[j,"vX"] += df.iloc[j]["a"][0]
         df.ix[j,"vY"] += df.iloc[j]["a"][1]
         df.ix[j,"vZ"] += df.iloc[j]["a"][2]
         df.ix[j,"pX"] += df.iloc[j]["vX"]
         df.ix[j,"pY"] += df.iloc[j]["vY"]
         df.ix[j,"pZ"] += df.iloc[j]["vZ"]
    lastVals.append(len(df))
    if len(lastVals) == 20:
        if lastVals.count(lastVals[0]) == 20: break

print(len(df))