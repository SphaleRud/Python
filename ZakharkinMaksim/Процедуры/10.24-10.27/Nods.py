def Nod_Minus(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return(a)

def Nod_Mod(a,b):
    while b>0:
        a,b=b,a%b
    return(a)
