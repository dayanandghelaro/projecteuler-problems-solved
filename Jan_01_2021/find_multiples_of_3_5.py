def find_multiples_of_3_5(n):
        l = []
        for i in range(2, n):
                if i%3 == 0 or i%5 == 0:
                        l.append(i)
        return sum(l)
find_multiples_of_3_5(10)
