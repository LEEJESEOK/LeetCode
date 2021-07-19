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
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        element = []

        def dfs(idx: int, n: int, k: int, element: int):
            if len(element) == k:
                results.append(element[:])
                return

            for i in range(idx, n):
                element.append(i + 1)
                dfs(i+1, n, k, element)
                element.pop()
            
            return

        dfs(0, n, k, element)

        return results


n, k = 4, 2
solution = Solution()
print(solution.combine(n, k))
