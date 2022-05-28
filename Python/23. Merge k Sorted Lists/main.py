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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None:
            return
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if amount else None
    
    def mergeLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = result = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
                
        node.next = l1 if l1 else l2
        
        return result.next
        