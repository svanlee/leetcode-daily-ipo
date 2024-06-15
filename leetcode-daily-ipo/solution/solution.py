import heapq
from typing import List

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        i, h = 0, []
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(h, -projects[i][0])
                i += 1
            if h:
                w -= heapq.heappop(h)
            else:
                break
        return w
