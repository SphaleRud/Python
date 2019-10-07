N=int(input("Введите N: "))
for i in range(1,N):
    b=10
    while i>=b:
        b=b*10
    if i*i%b==i:
        print(i,'*',i,'=',i*i)
