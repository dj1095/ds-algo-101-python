# From LeetCode Heaps [973. K Closest Points to Origin]
import heapq
import math
from typing import List, Final


class KClosestPointsToOrigin:
    ORIGIN: Final[List[int]] = [0, 0]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [[self.calc_euclidean_distance([0,0], point), point] for point in points]
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            item = heapq.heappop(minHeap)
            res.append(item[1])
            k -= 1
        return  res

    def calc_euclidean_distance(self, first_point, second_point) -> float:
        return (first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2



coord: List[List[int]] = [[3,3],[5,-1],[-2,4]]
num: int = 2
sol = KClosestPointsToOrigin()
result = sol.kClosest(coord, num)
print(result)
