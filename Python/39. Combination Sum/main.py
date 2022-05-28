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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(idx=0, combination=[], sum=0):
            if sum > target or idx not in range(len(candidates)):
                return
            elif sum == target:
                results.append(combination[:])
                return
            else:
                dfs(idx, combination +
                    [candidates[idx]], sum + candidates[idx])
                dfs(idx+1, combination, sum)

        dfs()

        return results


candidates, target = [2, 3, 6, 7], 7
solution = Solution()
print(solution.combinationSum(candidates, target))
