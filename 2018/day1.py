import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day1input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [int(x.strip()) for x in f.readlines()]

previousFrequencies = [0]
frequency = 0
done = False

while not done:
    for i in commands:
        frequency += i
        if frequency in previousFrequencies: 
            print(frequency)
            done = True
            break
        else:
            previousFrequencies.append(frequency)
    print(len(previousFrequencies))
