import numpy as np
from matplotlib import pyplot as plt

input_data = [x.strip() for x in open("./day8Input.txt", "r").readlines()][0]
part = 1

xsize, ysize = 25, 6
totalpix = xsize*ysize

totallayers = int(len(input_data) / totalpix)

fullImage = np.zeros((totallayers, xsize, ysize), dtype=np.uint8)

pixcount = 0
for i in range(totallayers):
    for y in range(ysize):
        for x in range(xsize):
            fullImage[i,x,y] = int(input_data[pixcount])
            pixcount += 1

zeroLayer = 0
fewestZeros = 6000

for i in range(totallayers):
    numZeros = totalpix - np.count_nonzero(fullImage[i])
    print(numZeros)
    if numZeros < fewestZeros:
        fewestZeros = numZeros
        zeroLayer = i

numOnes = np.sum(np.where(fullImage[zeroLayer] == 1, 1, 0))
numTwos = np.sum(np.where(fullImage[zeroLayer] == 2, 1, 0))

print(zeroLayer)
print(numOnes*numTwos)

finalImage = np.full((xsize,ysize), 2.0)
for i in range(xsize):
    for j in range(ysize):
        found = False
        for k in range(totallayers):
            if fullImage[k,i,j] != 2 and not found:
                finalImage[i,j] = fullImage[k,i,j]
                found = True

plt.imshow(finalImage)
plt.show()