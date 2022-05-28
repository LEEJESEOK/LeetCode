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
    def removeDuplicateLetters(self, s: str) -> str:
        # counter, stack = Counter(s), []

        # for char in s:
        #     counter[char] -= 1
        #     if char in stack:
        #         continue
        #     while stack and char < stack[-1] and counter[stack[-1]] > 0:
        #         stack.pop()
        #     stack.append(char)

        # return ''.join(stack)

        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


s = "cbacdcbc"
solution = Solution()
print(solution.removeDuplicateLetters(s))