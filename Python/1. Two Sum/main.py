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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr = nums[:]

        # for i in range(0, len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] + arr[j] == target:
        #             return [i, j]
        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums[i+1:]:
                return nums.index(num), nums[i+1:].index(complement)+i+1





# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
# nums = [3,3]
# target = 6


solution = Solution()
print(solution.twoSum(nums, target))