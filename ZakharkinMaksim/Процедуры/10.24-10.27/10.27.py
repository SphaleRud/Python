from Nods import Nod_Mod
from random import *
n=int(input("Введите количество цифр: "))
a=[randint(1,50) for i in range(n)]
print(*a)
x=0
for i in range(n):
    x=Nod_Mod(a[i],x)
print(x)
