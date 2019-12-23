from random import sample
 
num = int(input("Введите количество случайных чисел: "))
 
mass = sample(range(100), num) 
n = 1 
while n < len(mass):
     isChange = False
     for i in range(len(mass)-n):
          if mass[i] > mass[i+1]:
               mass[i],mass[i+1] = mass[i+1],mass[i]
               isChange = True
     n += 1
     if not isChange:
        break
 
print(*mass)
