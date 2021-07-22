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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for k, v in prerequisites:
            graph[k].append(v)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


# numCourses, prerequisites = 2, [[1,0]]
# numCourses, prerequisites = 2, [[1,0],[0,1]]
# numCourses, prerequisites = 5, [[1, 4], [2, 4], [3, 1], [3, 2]]
numCourses = 3
prerequisites = [[1, 0], [2, 0], [0, 2]]

solution = Solution()
print(solution.canFinish(numCourses, prerequisites))
