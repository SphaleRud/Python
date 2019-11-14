from random import *
c=[randint(1,1000) for i in range(100)]
print(*c)
M=c[0]
iM=0
for i in range(100):
    if c[i]>M:
        M=c[i]
        iM=i
print("В книге {:d} наибольшее количество страниц: {:d}".format(iM,M))
