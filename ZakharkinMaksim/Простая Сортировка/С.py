def summ (m):
    s = 0
    while m > 0:
        s += m%10
        m = m//10
    return s

from random import *
N=int(input("Введите количество цифр: "))
a=[randint(10,50) for i in range(N)]

print("До изменения: ",*a)

for i in range(N-1):
    for j in range(N-i-1):
        if summ(a[j]) > summ(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]         
a.reverse()

print("После изменения: ",*a)
