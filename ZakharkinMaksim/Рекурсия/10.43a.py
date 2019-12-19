def summ(num):
    return num%10 + summ(num//10) if num > 9 else num
a=int(input())
print(summ(a))

