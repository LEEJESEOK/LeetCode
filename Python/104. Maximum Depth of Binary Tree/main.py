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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         nodes = [root]

#         level = 0
#         while root and nodes:
#             level += 1

#             nodes = [
#                 child for node in nodes for child
#                 in {node.left, node.right} if child
#             ]

#         return level


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        level = 0

        while queue:
            level += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return level


root = [3, 9, 20, None, None, 15, 7]
solution = Solution()
print(solution.maxDepth(root))
