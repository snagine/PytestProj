import heapq
from collections import Counter
class HeapAlgos:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # turns an array into a heap in linear time
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0

    def heapDemo(self):
        heap = [67, 341, 234, -67, 12, -976]
        heapq.heapify(heap)

        heapq.heappush(heap, 7451)
        heapq.heappush(heap, -5352)

        # The numbers will be printed in sorted order
        while heap:
            print(heapq.heappop(heap))

    def getWrongAnswers(self, N: int, C: str) -> str:
        new = ['B' if C[i] == 'A' else 'A' for i in range(len(C))]
        return "".join(new)

    def getHitProbability(self,R: int, C: int, G: list[list[int]]) -> float:
        # Write your code here
        # zeros = count(G)
        ones = 0
        for i in range(R):
            ones += G[i].count(1)
        return ones / (R * C)

N = 3
C = 'ABA'

heapAlgos = HeapAlgos()
# res = heapAlgos.lastStoneWeight([2, 7, 4, 1, 8, 1])
# res = heapAlgos.topKFrequent([1, 1, 1, 2, 2, 3], 2)
# res = heapAlgos.getWrongAnswers(N, C)
res = heapAlgos.getHitProbability(2,3,[[0,0,1],[1,0,1]])
print(res)