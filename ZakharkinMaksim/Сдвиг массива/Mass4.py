from random import *
N=int(input("Введите размер массива: "))
a=[randint(0,100) for i in range(N)]
print("Массив:\n",*a)
pol=int(N/2)
b=0
for i in range(N-pol):
    k=a[b]
    a[b]=a[b+1]
    a[b+1]=k
    b+=2
print('Результат:\n',*a)
