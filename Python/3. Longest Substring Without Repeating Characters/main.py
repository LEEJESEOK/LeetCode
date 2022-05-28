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
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()

        length = start = 0

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                length = max(length, i-start + 1)
            used[c] = i

        return length

# s = "abcabcbb"
# s = "pwwkew"
# s = "aab"
s = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
