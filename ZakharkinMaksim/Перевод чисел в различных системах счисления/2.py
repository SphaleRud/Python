def change8(a,x):
    if x!=10:
        buffer=''
        while a>0:
            buffer=str(a%x)+buffer
            a=a//x
        return buffer
    else:
        print("Вы ввели не правильную систему счисления.")

num=int(input("Введите число в 10ой системе: "))
sys=int(input("Введите систему счисления в которую хотите перевести: "))
print('Число {:d} в 10ой системе, будет в 8ой системе - {:s}'.format(num,change8(num,sys)))
        
