from quick import *
from random import *

n=int(input("Введите размер списка: "))
A = [randint(0,10) for i in range(n)]
print(*A)
quick_sort(A)
print(*A)

count = 0
unique = []
for x in A:
    if x not in unique:
        count += 1
        unique.append(x)
print('Различных чисел:\n ',len(unique))
