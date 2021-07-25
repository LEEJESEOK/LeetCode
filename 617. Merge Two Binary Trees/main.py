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


### Recursion DFS
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node

        else:
            return root1 or root2


### Iterative
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        
        stack = collections.deque()
        stack.append([root1, root2])
        while stack:
            left, right = stack.pop()
            if left is None or right is None:
                continue
            left.val += right.val

            if left.left is None:
                left.left = right.left
            else:
                stack.append([left.left, right.left])
            if left.right is None:
                left.right = right.right
            else:
                stack.append([left.right, right.right])

        return root1
            

