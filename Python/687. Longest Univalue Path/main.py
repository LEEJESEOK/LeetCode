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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest = 0

        def univaluePath(node: TreeNode):
            nonlocal longest

            if node is None:
                return 0

            l = univaluePath(node.left)
            r = univaluePath(node.right)

            left, right = 0, 0
            if node.left and node.val == node.left.val:
                left = l + 1
            if node.right and node.val == node.right.val:
                right = r + 1

            longest = max(longest, left + right)
            return max(left, right)

        univaluePath(root)

        return longest