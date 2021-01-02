def gcd(a, b):
    if a%b != 0:
        return gcd(b, a%b)
    else:
        return b

def smallestMultiple(n=20):
    sM = 1
    for i in range(2, n+1):
        sM = sM*i//gcd(sM,i)

    return sM
