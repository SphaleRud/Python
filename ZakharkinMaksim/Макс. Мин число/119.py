from random import *
c=[randint(0,10) for i in range(50)]
print(*c)
M=c[0]
m=c[0]
kM=0
km=0
for i in range(50):
    if c[i]>M:
        M=c[i]
    if c[i]<m:
        m=c[i]
for f in range(50):
    if c[f]==M:
        kM+=1
    if c[f]==m:
        km+=1
print("Минимальных чисел - {:d} \nМаксимальных чисел - {:d}".format(km,kM))
