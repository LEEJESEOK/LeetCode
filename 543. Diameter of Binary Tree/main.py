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


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def diameter(node):
            if node is None:
                return 0

            l = diameter(node.left)
            r = diameter(node.right)

            self.result = max(self.result, l + r)
            return max(l, r) + 1

        diameter(root)

        return self.result


root = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.diameterOfBinaryTree(root))
