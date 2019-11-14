from random import *
c=[randint(150,227) for i in range(25)]
print(*c)
M=c[0]
m=c[0]
for i in range(25):
    if c[i]>M:
        M=c[i]
    if c[i]<m:
        m=c[i]
raz=M-m
print("Рост самого выского человека({:d}) различается от самого маленького человека({:d}) на {:d}".format(M,m,raz))
