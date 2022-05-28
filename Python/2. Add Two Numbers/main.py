import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        
        if node1 is None and node2 is None:
            return
        
        result = None
        node = result
        carry = 0
        while node1 or node2 or carry:
            if node1 is not None:
                val1 = node1.val
            else:
                val1 = 0
            if node2 is not None:
                val2 = node2.val
            else:
                val2 = 0
            
            val = val1 + val2 + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
                
            if result is None:
                result = ListNode(val)
                node = result
            else:
                valNode = ListNode(val)
                node.next = valNode
                node = valNode
                
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
            
        return result

l1 = [2,4,3], l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))