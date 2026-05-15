import heapq
n = int(input())
bids = list(map(int, input().split()))
pq = []
for i in bids:
    heapq.heappush(pq,-i)
highest = -heapq.heappop(pq)
print("Highest: ", highest)
if pq:
    print("Second Highest: ",-heapq.heappop(pq))