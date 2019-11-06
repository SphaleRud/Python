from random import *
c=[]
for i in range(1,41):
    c.append(randint(1,50))
print("До перемешивания: ",*c)
shuffle(c)
print("После перемешивания: ",*c)
