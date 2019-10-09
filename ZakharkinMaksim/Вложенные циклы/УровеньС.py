a,b=map(int,input("Введите границы диапозона: ").split())
for chisl in range(a,b+1):
    f=0
    for i in range(2,chisl):
        if chisl%i==0 and i!=chisl:
            f=1
            break
    if f<=0:
        print(chisl)
