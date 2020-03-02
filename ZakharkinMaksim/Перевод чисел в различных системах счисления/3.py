def rchange(a,x):
    if x!=10:
        lenN=len(a)
        buffer=0
        for i in range(lenN):
            buffer=buffer+int(a[i])*(x**(lenN-i-1))
        return buffer
    
num=input("Введите число: ")
sys=int(input("Введите систему счисления: "))
print("Число {:s} является числом в 10ой системе - {:d}".format(num,rchange(num,sys)))
