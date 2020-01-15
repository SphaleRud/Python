s=input('Введите ФИО: \n').split(' ')
print(*s,'\n')
b=[]
c=[]
for i in s[1]:
    b.append(i)
for i in s[2]:
    c.append(i)
print(b[0],'.',c[0],'. ',s[0])
