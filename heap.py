import heapq

heap=[5,9,8,3]
heapq.heapify(heap)
heapq.heappop(heap)
heapq.heappush(heap,6)
heapq.heappush(heap,9)
node=heapq.heappop(heap)
minNode=heapq.heappop(heap)
print(minNode)

maxNode=heapq.heappop(heap)
print(maxNode)
print(heap)

heap2=["Mary","Jane","Ann"]
heapq.heapify(heap2)
heapq.heappop(heap2)
heapq.heappush(heap2,"Jina")
print(heap2)
