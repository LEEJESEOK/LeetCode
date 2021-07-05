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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        
        if head is None:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        if q[:] != q[::-1]:
            return False
        
        return True


head = [1,2,2,1]
# head = [1,2]

solution = Solution()
print(solution.isPalindrome(head))