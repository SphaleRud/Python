from random import *
c=[randint(-1000,1000) for i in range(20)]
print(*c,'\n')

print("Номера элементов, которые оканчиваются на 4: ", end=" ")
for i in range(20):
    if c[i] >= 0:
        if c[i]%10 == 4:
            print(i)
    elif c[i] < 0:
        if c[i]%10 == 6:
            print(i)
