def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= 1
    return fact
n,k = map(int,input().split())
result = factorial(n)//((factorial(k))*factorial(n-k))
print(result)