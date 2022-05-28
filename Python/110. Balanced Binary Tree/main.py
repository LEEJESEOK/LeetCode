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
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        left_height = root.left.val if root.left else 0
        right_height = root.right.val if root.right else 0

        root.val = max(left_height, right_height) + 1
        return False if abs(left_height - right_height) > 1 else (left and right)
