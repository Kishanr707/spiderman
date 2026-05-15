def mod(a,m,p):
    result = 1
    a = a%p
    while m>0:
        if (m%2==1):
            result=(result*a)%p 
        a=(a*a)%p
        m=m//2
    return result
a,m,p = map(int,input().split())
print(mod(a,m,p))