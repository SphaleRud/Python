from random import *
from math import *
N=int(input("Введите размер массива: "))
a=[randint(0,100) for i in range(N)]
print("Массив:\n",*a)
pol=int(N/2)
pol1=a[:pol]
for i in range(pol):
    a[i]=a[i+pol]
k=0
for i in pol1:
    a[k+pol]=i
    k+=1
print("Результат:\n",*a)
