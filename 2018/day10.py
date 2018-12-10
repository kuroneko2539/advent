import argparse, numpy as np, re
import matplotlib.pyplot as plt
import time

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day10input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

positions = []
velocities = []
for command in commands:
    vals = re.findall("<.*?>", command)
    pos = vals[0][1:-1].split(",")
    vel = vals[1][1:-1].split(",")
    positions.append([int(pos[0]), int(pos[1])])
    velocities.append([int(vel[0]), int(vel[1])])
count = 0
while True:
    count += 1
    for point in range(len(positions)):
        positions[point][0] += velocities[point][0]
        positions[point][1] += velocities[point][1]
    if count == 10521:
        for point in range(len(positions)):
            plt.scatter(positions[point][0], positions[point][1], color="black")
        plt.savefig("./day10/count{}.jpg".format(count))
        plt.close()