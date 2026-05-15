a,b,p,k = map(int,input().split())
mod = (a%p * b%p)%p
if mod%k==0:
    print("Divisible")
else:
    print("Not divisible")