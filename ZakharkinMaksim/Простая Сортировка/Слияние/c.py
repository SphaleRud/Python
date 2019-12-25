def middle(num,N):
    return num/N

from random import *

N=int(input()) #Количество цифр

a=[randint(0,100) for i in range(N)]
b=[randint(0,100) for i in range(N)]

p=0
#Сортировка слиянием
for i in range(N-1):
    nMin=i
    for j in range(i+1,N):
        if a[j]<a[nMin]:
            nMin=j
            p+=1
    if i!=nMin:
        a[i],a[nMin]=a[nMin],a[i]
print("Среднее количество процедур 'Слиянием': ",middle(p,N))

k=0
#Сортировка "Пузырьком"
for i in range(N-1):
    for j in range(N-2,i-1,-1):
        if b[j+1]<b[j]:
            b[j],b[j+1]=b[j+1],b[j]
            k+=1
print("Среднее количество процедур 'Пузырьком': ",middle(k,N))
