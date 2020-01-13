from quick import *
from random import *

n=int(input("Введите размер списка:\n"))
a=[randint(0,10) for i in range(n)]
print('Массив:\n',*a)
a=quicksort(a)
print('После сортировки:\n',*a)

x=int(input("Введите число x:\n"))
y=0
l=1;r=n
while l<r-1:
    c=(l+r)//2
    if x<a[c]:
        r=c
        y+=1
    else:
        l=c
        y+=1
        
if a[l]==x:
    print('Число',x,"найдено.")
else:
    print('Число',x,"не найдено.")

print("Количество сравнений: ",y)
