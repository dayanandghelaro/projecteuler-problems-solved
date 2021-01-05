def sumOfSquaresOfNNaturalNos(n):
    return (n*(n+1)*(2*n+1))//6
def squaresOfSumOfNNaturalNos(n):
    return (n*(n+1)//2)**2


def difference(n):
    x = sumOfSquaresOfNNaturalNos(n)
    y = squaresOfSumOfNNaturalNos(n)
    print(x)
    print(y)
    if x>y:
        r = x-y
    else:
        r = y-x
    return r

print(difference(100))
