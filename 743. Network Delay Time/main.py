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
    result = -1
    largest = []  

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        discovered = []
        stack = []

        course = collections.defaultdict(list)
        for u, v, w in times:
            course[u].append((v, w))

        def dfs(u: int):
            for v, w in course[u]:
                discovered.append(v)
                dfs(v)

        discovered.append(k)
        stack.append(k)
        dfs(k)

        print(self.largest)

        return self.result if len(discovered) == n else False


times, n, k = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
solution = Solution()
print(solution.networkDelayTime(times, n, k))
# print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
# print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
