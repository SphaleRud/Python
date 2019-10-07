N=int(input("Введите N: "))
for i in range(N):
    for j in str(i):
        ji = int(j)
        if ji != 0 and ji != 1 and i % ji:
            break
    else:
        print(i),
