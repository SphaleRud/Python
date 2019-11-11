from random import *
c=[randint(-1000,1000) for i in range(20)]
print(*c,'\n')
for i in range(20):
    if i%3 == 0:
        print(i,'=',c[i],end=', ')
print('\n')
for f in range(20):
    if f%4 == 0:
        print(f,'=',c[f],end=', ')
