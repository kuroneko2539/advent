A = 618
B = 814

def nextAandB(A, B):
    while True:
        A = A * 16807
        A = A % 2147483647
        if A % 4 == 0:
            break

    while True:
        B = B * 48271
        B = B % 2147483647
        if B % 8 == 0:
            break
    return A, B

goodCount = 0

for _ in range(5000000):
    A, B = nextAandB(A,B)

    if (bin(A)[-16:] == bin(B)[-16:]): goodCount += 1
    
print(goodCount)