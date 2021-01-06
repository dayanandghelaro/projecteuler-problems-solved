def getNextTerm():
    i = 1
    while True:
        i = i+ 1
        x = int((1/2)*(i**2 + i))
        yield x
def getNOfDivisors(n):
    count = 2
    for i in range(2, n):
        if n%i == 0:
            count+=1
    return count    
g = getNextTerm()
while True:
    n = next(g)
    nOfDivisors = getNOfDivisors(n)
    print('number of divisors of %s : '%n, nOfDivisors)
    if nOfDivisors >= 500:
        break

