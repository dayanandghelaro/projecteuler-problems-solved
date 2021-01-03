import math
def isPrime(p):
    if p == 2 or p == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(p))+1):
            if p%i == 0:
                return False
        return True
def nextPrimeNumber():
    p = 1
    while True:
        p += 1
        if isPrime(p):
            yield p

#g = nextPrimeNumber()
#for i in range(20):
#    print(next(g))

def largestPrimeFactor(n):
    g = nextPrimeNumber()
    factors = []
    while not isPrime(n):
        x = next(g)        
        #print(x)
        if n%x == 0:
            factors.append(x)
            n = n//x
            g = nextPrimeNumber()
    factors.append(n)
    return factors
print(max(largestPrimeFactor(13195)))
print(max(largestPrimeFactor(600851475143)))
