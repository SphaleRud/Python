from random import *
c=[randint(-1000,1000) for i in range(20)]
flag1=False
flag2=False
k=0
v=0
print(*c)
print("\nA):",end=' ')
for i in range(20):
    if c[i]<10 or c[i]>=100:
        k+=1
    if abs(c[i])//10<10 and abs(c[i])//10!=0:
        print(c[i],end=' ')
    elif k==20:
        flag1=True
if flag1:
    print("Двухзначных чисел нет.")
print("\nB):",end=" ")
for f in range(20):
    if c[i]<10 or c[i]>=100:
        v+=1
    if c[f]//100 < 10 and c[f]//100 > -11 and c[f]//100!=-1 and c[f]//100!=0:
        print(c[f],end=' ')
    elif v==20:
        flag2=True
if flag2:
    print("Трехзначных чисел нет.")

