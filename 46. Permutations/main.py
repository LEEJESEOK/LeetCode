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
    def permute(self, nums: List[int]) -> List[List[int]]:
        prevElements = []
        result = []

        def dfs(elements: List[int]):
            if len(elements) == 0:
                if prevElements not in result:
                    result.append(prevElements[:])

            for e in elements:
                nextElement = elements[:]
                nextElement.remove(e)

                prevElements.append(e)
                dfs(nextElement)
                prevElements.pop()

        dfs(nums)

        return result


nums = [1, 1, 2]
# nums = [1, 2, 3]
solution = Solution()
print(solution.permuteUnique(nums))
