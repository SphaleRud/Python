from random import *
c=[randint(-1000,1000) for i in range(20)]
print(*c,'\n')
for i in range(20):
    if c[i]%3 == 0:
        print("A[{:d}]={:d}".format(i,c[i]),end=', ')
print('\n')
for f in range(20):
    if c[f]%4 == 0:
        print("A[{:d}]={:d}".format(f,c[f]),end=', ')
