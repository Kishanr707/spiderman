n =int(input())
arr = list(map(int,input().split()))
checksum = int(input())
ans = 0
for i in ans:
    ans ^= i
if ans == checsum:
    print("OK")
else:
    print("ANOMALY")