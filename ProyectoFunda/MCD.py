def MCD(numA, numB):
    if numB == 0:
        return numA
    else:
        return MCD(numB, numA%numB)

a = 18
b = 48

print(MCD(a, b))