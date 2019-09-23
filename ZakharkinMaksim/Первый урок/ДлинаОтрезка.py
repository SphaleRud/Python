from math import sqrt

print('Введите координаты точки А:')
x1,y1 = map(float, input().split()) #Координаты точки А
print('Введите координаты точки B:')
x2,y2 = map(float, input().split()) #Координаты точки B
AB = sqrt((x2-x1)**2+(y2-y1)**2) #Вычесление длины отрезка
print('Длинна отрезка АВ = {:5.3f}'.format(AB))
