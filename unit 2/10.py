def demo():
    n = 5
    while n>0:
        yield n
        n -= 1


for i in demo():
    print(i)