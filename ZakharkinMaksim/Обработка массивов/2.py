from random import *
c=[randint(-1000,1000) for i in range(20)]
flag1=True
flag2=True
for i in range(20):
    if c[i] >= 0:
        print(c[i])
    else:
        flag1=False
for i in range(20):
    if c[i] < 0:
        print(c[i])
    else:
        flag2=False
if flag1:
    print("Отрицательных цифр нет.")
if flag2:
    print("Положительных цифр нет.")
