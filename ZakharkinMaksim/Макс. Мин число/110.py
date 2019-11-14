from random import *
c=[randint(1,250) for i in range(20)]
print(*c)
m=c[0]
for i in range(20):
    if c[i]<m:
        m=c[i]
print("Самые дешевые конфеты стоят {:d} рублей".format(m))
