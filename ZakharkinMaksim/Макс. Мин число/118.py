from random import *
c=[randint(2000,2010) for i in range(30)]
print(*c)
M1=c[0]
iM1=0
M2=c[1]
iM2=0
k=0
for i in range(30):
    if c[i]<M1:
        M1=c[i]
        iM1=i
for i in range(30):
    if c[i]==M1:
        k+=1
        M2=c[i]
        iM2=i
if k>1:
    print("\nПервый родился под номером {:d} \nПоследний родился под номером {:d}".format(iM1,iM2))
else:
    print("\nСамый старший человек под номером {:d}".format(iM1))
