from random import *
N=int(input("Введите размер массива: "))
a=[randint(0,100) for i in range(N)]
print("Массив:\n",*a)
k=0
for i in range(N):
    if a[i]%2>0:
        k=a[i]
if k>0:
    for i in range(N):
        if a[i]%2>0:
            a[i]=k+a[i]
else:
    print("Нечетных чисел нет.")
print("Результат:\n",*a)
