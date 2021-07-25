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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return

        queue = collections.deque([root])
        result = []
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            level += 1

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return
        
        root = TreeNode(data[0])
        queue = collections.deque([root])
        i = 1

        while queue and i <= len(data)-1:
            node = queue.popleft()

            if data[i] is not None:
                left = TreeNode(data[i])
                node.left = left
                queue.append(left)
            i += 1

            if i > len(data) - 1:
                break
            if data[i] is not None:
                right = TreeNode(data[i])
                node.right = right
                queue.append(right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
