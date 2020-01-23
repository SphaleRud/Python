a=input('Введите три числа с знаком: ')
print(a)
minus=0
minus1=0
de=0
um=0
b=0
for i in range(len(a)):
    if a[i]=='-' and i != 0:
        minus1=i
        break  
for i in range(len(a)):
    if a[i]== '-':
        minus=i
    if a[i]=='+':
        b=i
    if a[i]=='*':
        um=i
    if a[i]=='/':
        de=i
plus=0
for i in range(len(a)):
    if a[i] in ('-','+','*','/') and i!=0:
        plus=int(a[:i])
        break

for i in range(len(a)):
    if a[i] == '*' and i<b:
        plus=plus*int(a[i+1:b])
    elif a[i] == '*' and i<minus:
        plus=plus*int(a[i+1:minus])
    elif a[i]=='*' and i<um:
        plus=plus*int(a[i+1:um])    #Умножение
    elif plus=='*' and i<de:
        plus=plus*int(a[i+1:de])
    elif a[i]=='*':
        plus=plus*int(a[i+1:])

for i in range(len(a)):
    if a[i] == '+' and i < b:
        plus=plus+int(a[i+1:b])
    elif a[i]=='+' and i<minus:
        plus=plus+int(a[i+1:minus])
    elif a[i]=='+' and i<um:
        plus=plus+int(a[i+1:um])
    elif a[i]=='+' and i<de:
        plus=plus+int(a[i+1:de])
    elif a[i] == '+':
        plus=plus+int(a[i+1:])
        
    if a[i]== '-' and i != 0:
        if i>=minus1 and i < minus:
            plus=plus+int(a[i:minus])
        elif i==minus and i < b:
            plus=plus+int(a[i:b])
        elif i==minus:
            plus=plus+int(a[i:])
print(plus)
        
