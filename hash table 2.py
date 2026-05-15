n = int(input())
books = {}
for i in range(n):
    title, bid = input().split()
    books[title] = int(bid)

q = int(input())
for i in range(q):
    query = input().strip()
    if query in books:
        print(books[query])
    else:
        print("Not found")