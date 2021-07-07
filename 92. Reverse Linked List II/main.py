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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return
        
        nodeStack = []
        
        node = head
        resultNode = result = ListNode()
        
        count = 0
        while node is not None:
            count += 1
            if left <= count and count <= right:
                nodeStack.append(node.val)
            
            node = node.next
        
        node = head
            
        count = 0
        while node is not None:
            count += 1
            if left <= count and count <= right:
                resultNode.next = ListNode(nodeStack.pop())
            else:
                resultNode.next = node
            resultNode = resultNode.next
            node = node.next
        
        return result.next
            