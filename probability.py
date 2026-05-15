def combination(n,k):
    if k>n:
        return 0
    result = 1
    k = min(k, n-k)
    for i in range(1, k+1):
        result = (result*(n-i+1))//i
    return result
k,r = map(int,input().split())
favor = combination(13,r) * combination(39,k-r)
total = combination(52,k)
probability = favor/total
print(f"{probability:.6f}")