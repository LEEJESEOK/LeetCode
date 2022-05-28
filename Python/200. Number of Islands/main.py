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
    def numIslands(self, grid: List[List[str]]) -> int:
        discovered = []
        island = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    island += 1
                    self.dfs(grid, y, x)

        return island

    def dfs(self, grid: List[List[str]], y: int, x: int) -> int:
        if (y < 0) or y > len(grid) - 1 or x < 0 or x > len(grid[y]) - 1 or grid[y][x] == "0":
            return

        grid[y][x] = "0"

        self.dfs(grid, y - 1, x)
        self.dfs(grid, y + 1, x)
        self.dfs(grid, y, x - 1)
        self.dfs(grid, y, x + 1)


# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
print(solution.numIslands(grid))
