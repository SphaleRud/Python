a,b = map(int,input('Введите границы диапозона: ').split())
for i in range(a, b+1): 
    prime = True    
    for j in range(a, i):
        if i%j == 0:
            prime = False
            break 
        elif prime:
            print(i)
