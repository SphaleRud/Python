from random import *
c=[randint(-1000,1000) for i in range(20)]
print(*c)
for i in range(20):
    if c[i]%10 == 0:
        c[i]=0
print('\nA): ',*c)
for i in range(20):
    if c[i]%2 == 0:
        c[i]=int(c[i]/2)
    else:
        c[i]=int(c[i]*2)
print('\nB): ',*c)
m,n=map(int,input("\nВведите во сколько раз уменишить, и во сколько увеличить: ").split())
for i in range(20):
    if c[i]%2 > 0:
        c[i]=c[i]-m
    elif i%2 > 0:
        c[i]=c[i]+n
print('\nC): ',*c)
        
