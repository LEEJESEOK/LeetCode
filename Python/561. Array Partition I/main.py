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
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0

        nums.sort()
        for i in range(0, len(nums), 2):
            result += min([nums[i], nums[i+1]])
        return result

        # return sum(sorted(nums)[::2])


# nums = [1,4,3,2]
nums = [6,2,6,5,1,2]


solution = Solution()
print(solution.arrayPairSum(nums))