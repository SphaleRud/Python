a=input('Введите три числа с знаком: ')
print(a)
minus=0
minus1=0
b=0
for i in range(len(a)):
    if a[i]=='-' and i != 0:
        minus1=i
        break  
for i in range(len(a)):
    if a[i]== '-':
        minus=i
    if a[i]== '+':
        b=i
        
plus=0
for i in range(len(a)):
    if a[i]=='-' and i!=0:
        plus=int(a[:i])
        break
    if a[i]=='+':
        plus=int(a[:i])
        break

for i in range(len(a)):
    if a[i] == '+':
        plus=plus+int(a[i+1])
    if a[i]== '-' and i != 0:
        if i>=minus1 and i < minus:
            plus=plus+int(a[i:minus])
        elif i==minus and i < b:
            plus=plus+int(a[i:b])
        elif i==minus:
            plus=plus+int(a[i:])
print(plus)
        
