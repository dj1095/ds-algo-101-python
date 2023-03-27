# From LeetCode Heaps [215. Kth Largest Element in an Array]
import heapq
from typing import List


class KthLargestElement:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k - 1 > 0:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)


numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6]
n = 4
sol = KthLargestElement()
res = sol.findKthLargest(numbers, n)
print(res)
