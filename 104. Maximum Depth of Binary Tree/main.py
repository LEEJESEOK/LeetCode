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
        if not root:
            return 0
        queue = [root]

        level = 0
        while queue:
            level += 1
            task=[]
            queue.reverse()
            i = 0
            while queue:
                task.append(queue.pop())
                i += 1
            for n in task:
                if n:
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)

        return level


root = [3,9,20,None,None,15,7]
solution = Solution()
print(solution.maxDepth(root))