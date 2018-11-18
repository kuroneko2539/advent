import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day4input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    inputLines = f.readlines()


##PART 1: no duplicate words

goodCount = 0
print(len(inputLines))
for line in inputLines:
    goodPass = True
    words = [x.strip() for x in line.split(" ")]
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                goodPass = False
                break
        if not goodPass: break
    if goodPass: goodCount += 1
print(goodCount)

##PART 2: no anagrams either

goodCount = 0
print(len(inputLines))
for line in inputLines:
    goodPass = True
    words = [x.strip() for x in line.split(" ")]
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if sorted(words[i]) == sorted(words[j]):
                goodPass = False
                break
        if not goodPass: break
    if goodPass: goodCount += 1
print(goodCount)