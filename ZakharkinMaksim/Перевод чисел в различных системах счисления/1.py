def change8(a):
    buffer=''
    while int(a)>0:
        buffer=str(int(a)%8)+buffer
        a=int(a)//8
    return buffer

num=input("Введите число в 10ой системе:")
print('Число {:s} в 10ой системе, будет в 8ой системе - {:s}'.format(num,change8(num)))
        
