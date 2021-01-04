import math
primesDict = {}
def isPrime(p):
    global primesDict
    if p == 2 or p == 3:
        return True
    else:
        for i in primesDict.values():
            if p%i == 0:
                return False
        return True
def nextPrimeNumber():
    global primesDict
    p = 1
    while True:
        p += 1
        if isPrime(p):
            primesDict[str(p)] = p
            yield p

def nthPrime(n):
    if n>=2:
        p = 2
    else:
        p = -1
    g = nextPrimeNumber()
    for i in range(n):
        p = next(g)
        print(str(i+1)+"  --- ", p)
    return p
print(nthPrime(10001)) # 104743
