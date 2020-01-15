s=input('Введите адрес файла: \n').split()
g=input('Что меняем: ')
h=input('Чем заменить: ')
for i in range(len(s)):
    if s[i]== g:
        s[i]=h
print(*s)
