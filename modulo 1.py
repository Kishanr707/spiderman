n,m = int(input())
arr=list(map(int,input().split()))
total = 0
for i in range(n):
    total = (total+i)%m 
print(total)