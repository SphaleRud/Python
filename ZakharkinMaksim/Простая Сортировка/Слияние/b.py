from random import *
N=int(input())
a=[randint(0,10) for i in range(N)]
print(*a)
for i in range(N-1):
    nMin=i
    for j in range(i+1,N):
        if a[j]<a[nMin]:
            nMin=j
    if i!=nMin:
        a[i],a[nMin]=a[nMin],a[i]
p=0
unique=[]
for i in a:
    if i not in unique:
        p+=1
        unique.append(i)
print(*a)
print(p)
