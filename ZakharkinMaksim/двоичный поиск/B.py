from quick import *
from random import *

n=int(input("Введите размер списка:\n"))
a=[randint(0,10) for i in range(n)]
print('Массив:\n',*a)
a=quicksort(a)
print('После сортировки:\n',*a)

x=int(input("Введите число x:\n"))
y=0
b=[]
for i in range(n//2):
    l=0;r=n
    while l<r-1:
        c=(l+r)//2
        if x<a[c]:
            r=c
        else:
            l=c
    if a[l]==x:
        b=a.pop(l)
        y+=1
if y>0:
    print('Число',x,'встречается',y,"раз(а).")
else:
    print("Число",x,"не встречается")

            
