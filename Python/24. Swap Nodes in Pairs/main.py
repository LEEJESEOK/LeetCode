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
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        node = result = ListNode()
        
        while head is not None and head.next is not None:
            fast = head.next
            slow = head
            node.next = ListNode(fast.val)
            node = node.next
            node.next = ListNode(slow.val)
            node = node.next
            
            head = head.next.next
            
        if head is not None:
            node.next = ListNode(head.val)
        
    
        return result.next