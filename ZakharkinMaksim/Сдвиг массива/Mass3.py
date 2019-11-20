from random import *
N=int(input("Введите размер массива: "))
a=[randint(0,100) for i in range(N)]
print("Массив:\n",*a)
iM=0
M=a[0]
im=0
m=a[0]
for i in range(N):
    if a[i]>M:
        M=a[i]
        iM=i
    if a[i]<m:
        m=a[i]
        im=i
buf=M
a[iM]=m
a[im]=buf
print("Результат:\n",*a)
