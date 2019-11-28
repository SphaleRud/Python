from math import *
def Summ_P(a,b,h1,d,e,h2):
    ak=int((a-b)/2)
    ab=sqrt(ak**2+h1**2)
    ak2=int((d-e)/2)
    ab2=sqrt(ak2**2+h2**2)
    print((2*ab+a+b)+(2*ab2+d+e))
def Summ_S(a,b,h1,d,e,h2):
    s1=(a+b)/2*h1
    s2=(d+e)/2*h2
    print(s1+s2)
    
