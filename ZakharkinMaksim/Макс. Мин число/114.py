from random import *
c=[randint(0,10) for i in range(8)]
print(*c)
M=c[0]
m=c[0]
for i in range(8):
    if c[i]>M:
        M=c[i]
    if c[i]<m:
        m=c[i]
print(m,M,'\n')
c.remove(M)
c.remove(m)
print(round(sum(c)/6))
