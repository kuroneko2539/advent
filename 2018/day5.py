import argparse, re, string

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day5input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]
    startString = commands[0]

lowestNum = 50000
lowestChar = ""
for remChar in string.ascii_lowercase:
    inString = startString.replace(remChar, "")
    inString = inString.replace(str.upper(remChar), "")

    while True:
        changes = 0
        pos = len(inString) - 1
        while pos > 0:
            char1 = inString[pos] 
            char2 = inString[pos-1]
            if (str.islower(char1) and str.isupper(char2)) or (str.isupper(char1) and str.islower(char2)):
                if str.lower(char1) == str.lower(char2):
                    changes += 1
                    inString = inString[:pos-1] + inString[pos+1:]
                    pos -= 1
            pos -= 1
        if changes == 0:
            break
    if len(inString) < lowestNum:
        lowestChar = remChar
        lowestNum = len(inString)
print(lowestChar, lowestNum)