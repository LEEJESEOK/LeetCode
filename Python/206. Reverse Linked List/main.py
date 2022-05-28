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
    def reverseList(self, head: ListNode) -> ListNode:
        nodeStack = []
        if head is None:
            return
        
        node = head
        while node is not None:
            nodeStack.append(node.val)
            node = node.next
            
        rev = ListNode(nodeStack.pop())
        node = rev
        while nodeStack != []:
            nextNode = ListNode(nodeStack.pop())
            tempNode = nextNode
            node.next = nextNode
            node = tempNode
        
        return rev

head = [1,2,3,4,5]

solution = Solution()
print(solution.reverseList(head))