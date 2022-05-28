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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


# nums, k = [1, 1, 1, 2, 2, 3], 2
nums, k = [3, 0, 1, 0], 1

solution = Solution()
print(solution.topKFrequent(nums, k))
