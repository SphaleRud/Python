from random import *
c=[randint(1,100) for i in range(20)]
print(*c)
M=c[0]
iM=0
m=c[0]
im=0
for i in range(20):
    if c[i]>M:
        M=c[i]
        iM=i
    if c[i]<m:
        m=c[i]
        im=i
Raz=M-m
print("Максимальный элемент: A[{:d}]={:d}".format(iM,M))
print("Минимальный элемент: A[{:d}]={:d}".format(im,m))
print("Максимальный элемент больше минимального на",Raz)
