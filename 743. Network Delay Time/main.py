# using common module in LeetCode
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]

        dist = collections.defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))

        return max(dist.values()) if len(dist) == n else -1


times, n, k = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
solution = Solution()
print(solution.networkDelayTime(times, n, k))
# print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
# print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
