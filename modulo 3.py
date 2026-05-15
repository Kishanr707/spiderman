def mod(a,m,p):
    result = 1
    a = a%p
    while m>0:
        if (m%2==1):
            result = (result*a)%p 
        a = (a*a)%p
        m = m//2
    return result
n,p = map(int,input().split())
total = 0
for i in range(n):
    a,m = map(int(input().split()))
    total = (total + mod(a,m,p))%p 
print(total)