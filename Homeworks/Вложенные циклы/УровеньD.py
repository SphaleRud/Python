a,b=map(int,input("Введите границы диапозона: ").split())
for i in range(a,b+1):
    f=0
    for j in range(1,5):
        for p in range(1,i+1):
            if i%j==0:
                f==0
    if f<=0:
        print(i)
