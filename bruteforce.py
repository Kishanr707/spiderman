text = input().strip()
pattern = input().strip()
m = len(text)
n = len(pattern)
found = False
for i in range(n - m + 1):
    while j < m and text[i + j] == pattern[j]:
        j += 1
    if j == m:
        found = True
        break
if found:
    print("Found")
else:
    print ("Not found")