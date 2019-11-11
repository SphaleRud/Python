from random import *
c=[randint(-1000,1000) for i in range(20)]
flag1=True
flag1=True
print(*c)
print("A):",end=' ')
for i in range(20):
    if c[i]//10 < 10 and c[i]//10!=0 and c[i]//10 > -10:
        print(c[i],end=' ')
    else:
        flag1=False
print("\nB):",end=" ")
for f in range(20):
    if c[f]//100 < 10 and c[f]//100 !=-1 and c[f]//100 > -10:
        print(c[f],end=' ')
    else:
        flag2=False
if flag1:
    print("Двухзначных чисел нет.")
if flag2:
    print("Трехзначных чисел нет.")

