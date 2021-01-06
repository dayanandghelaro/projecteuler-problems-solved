found = False
for i in range(1, 999):
    if found:
        break
    print(i)
    for j in range(1, 999):
        if found:
            break
        for k in range(1, 999):
            if ((i+j+k) == 1000) and (i**2 + j**2 == k**2):
                print('Found ')
                print(i)
                print(j)
                print(k)
                found = True
                break

"""
    Found 
    200
    375
    425
    multiplication = 31875000

"""
