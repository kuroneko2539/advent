import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day2input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputLines = f.readlines()


##PART 1: checksum = sum(max - min) per line
checksum = 0
for line in inputLines:
    contents = [int(x) for x in line.split("\t")]
    checksum += max(contents) - min(contents)

print(checksum)

##PART 2: checksum = sum(wholey divisible numbers) per line
checksum = 0
for line in inputLines:
    contents = [int(x) for x in line.split("\t")]
    lineComplete = False
    for i in range(len(contents)):
        for j in range(i+1,len(contents)):
            if int(float(contents[i])/float(contents[j])) == float(contents[i])/float(contents[j]):
                checksum += int(float(contents[i])/float(contents[j]))
                lineComplete = True
                break
            elif int(float(contents[j])/float(contents[i])) == float(contents[j])/float(contents[i]):
                checksum += int(float(contents[j])/float(contents[i]))
                lineComplete = True
                break
        if lineComplete: break

print(checksum)