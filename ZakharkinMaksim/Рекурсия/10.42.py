def power(a, n):
    if n==0:
        return 1
    return a*power(a, n-1)

a,b=map(int,input().split())
print(power(a,b))
