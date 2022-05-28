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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(elements: List[int] = [], idx: int = 0):
            if len(elements) == k:
                results.append(elements[:])
                return

            for i in range(idx, n):
                elements.append(nums[i])
                dfs(elements, i + 1)
                elements.pop()

        n = len(nums)
        for k in range(n + 1):
            dfs()

        return results


nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))
