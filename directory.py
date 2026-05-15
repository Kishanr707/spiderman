from collections import defaultdict
n = int(input())
tree = defaultdict(list)
file_index = {}
for i in range(n):
    directory, file = input().split()
    tree[directory].append(file)
    file_index = True
search = input()
for directory in tree:
    print(directory, *file[directory])
if search in file_index:
    print("found")
else:
    print("not found")