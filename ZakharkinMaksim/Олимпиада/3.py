tower=int(input("Введите количество башен: "))
high=[]
f1=0
print("Введите высоты башен: ",end="")
for h in input().split():
    high.append(int(h))
x=len(high)
if x==tower:
    K=int(input("Сколько выстрелов было произведенно: "))
    for i in range(K):
        a,b=map(int,input().split())
        aMax=high[a-1]
        for d in high[a:b]:
            if d>aMax:
                aMax=d
        print(aMax)
else:
    print("Вы ввели неправильное число")
            
        
