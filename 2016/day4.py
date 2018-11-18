import argparse
import numpy as np
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day4input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    rooms = [x.strip() for x in f.readlines()]

goodRooms = []

for room in rooms:
    counter = Counter([x for x in room[:-7] if str.isalpha(x)])
    sortedCount = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    hashkey = ""
    for i in range(5):
        hashkey += sortedCount[i][0]
    if hashkey == room[-6:-1]: goodRooms.append(room)

sectorIDTotal = 0
print(len(goodRooms))

for room in goodRooms:
    sectorIDTotal += int(room.split("[")[0].split("-")[-1])

print(sectorIDTotal)

decryptedRooms = []
for room in goodRooms:
    sectorID = int(room.split("[")[0].split("-")[-1])
    roomWords = room.split("[")[0].split("-")[:-1]
    decryptedWords = []
    for word in roomWords:
        decrypted = []
        for character in word:
            charID = ((ord(character) - 97 + sectorID) % 26) + 97
            decrypted.append(chr(charID))
        decryptedWords.append("".join(decrypted))
    decryptedRooms.append([sectorID,decryptedWords])

for room in decryptedRooms:
    if "northpole" in room[1]:
        print(room)
            