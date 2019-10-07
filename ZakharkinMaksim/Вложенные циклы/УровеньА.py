a,b,c=map(int,input("Введите вес ящиков: ").split())
v=0
for i in range(0,int(185/a)+1):
    for j in range(0,int(185/b)+1):
        for n in range(0,int(185/c)+1):
            if a*i+b*j+n*c==185:
                v=v+1
print(v)

