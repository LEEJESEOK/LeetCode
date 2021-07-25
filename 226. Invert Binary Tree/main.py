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


### Recursion
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:

#         def dfs(node: TreeNode) -> TreeNode:
#             if node is None:
#                 return

#             invertNode = TreeNode(node.val, dfs(node.right), dfs(node.left))

#             return invertNode

#         return dfs(root)


### Iterative BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root


### Iterative preorder DFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root


### Iterative postorder DFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left

        return root


root = [4, 2, 7, 1, 3, 6, 9]
solution = Solution()
print(solution.invertTree(root))
