# From LeetCode Heaps [1046. Last Stone Weight]
import heapq
from typing import List


class LastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones: List[int] = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return -stones[0]
            maxElement = -heapq.heappop(stones)
            secondMax = -heapq.heappop(stones)
            if maxElement - secondMax > 0:
                heapq.heappush(stones, secondMax - maxElement)

sol = LastStoneWeight()
weights = [2, 7, 4, 1, 8, 1]
result = sol.lastStoneWeight(weights)
print(result)
