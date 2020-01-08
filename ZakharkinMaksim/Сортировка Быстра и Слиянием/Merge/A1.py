from merge import *
from random import *

n=int(input("Введите размер списка: "))

A = [randint(0,100) for i in range(n)]
print(*A)
B1=merge_sort(A[:len(A)//2])
B2=merge_sort(A[len(A)//2:])
B2.reverse()

print(*B1,*B2) 
