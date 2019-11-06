a,b=map(int,input("Введите X и D: ").split())
c=[]

for i in range(20):
    a=a+b
    c.append(a)

for i in reversed(c):
    print(i,end = ' ')
