def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = 0
    merged = []
    while i<len(left) and j<len(right):
        if left[i][0]<right[j][0]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[i])
    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
        merged.append(right[j])
        j+=1
    return merged

n = int(input())
store = []
for i in range(n):
    time, bib = map(int,input()split())
    store.append((time,bib))
sorted= merge_sort(store)
for i in range(10):
    print(sorted[i][0],sorted[i][1])