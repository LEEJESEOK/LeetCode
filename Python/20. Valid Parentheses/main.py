import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        # if s is []:
        #     return True
        # if len(s) % 2 == 1:
        #     return False
            
        # open = []
        # openBracket = ''

        # for bracket in s:
        #     if bracket == '(' or bracket == '{' or bracket == '[':
        #         open.append(bracket)
        #     else:
        #         if len(open) > 0 and ((bracket == ')' and open[-1] == '(') or (bracket == '}' and open[-1] == '{') or (bracket == ']' and open[-1] == '[')):
        #             open.pop()
        #         else:
        #             return False

        # return open == []

        table = {
            ']':'[', 
            '}':'{',
            ')':'('}

        stack = []

        for bracket in s:
            if bracket not in table:
                stack.append(bracket)
            elif not stack or table[bracket] != stack.pop():
                return False
            
        return stack == []


s = "()"
solution = Solution()
print(solution.isValid(s))