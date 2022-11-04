prew = cur = 1
element = input('Введите число : ')
element = int(element)
for n in range(1,element-2):
    tmp = prew + cur
    prew = cur
    cur = tmp
print('Сумма ' + str(cur))
