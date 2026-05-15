n = int(input())
table =set()
for i in range(n):
    table.add(input())
q = int(input())
for i in range(q):
    query = input()
    if query in table:
        print("Found")
    else:
        print("Not found")