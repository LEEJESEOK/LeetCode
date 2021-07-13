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
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsList = list(jewels)
        answer = 0

        for stone in stones:
            if stone in jewelsList:
                answer += 1

        return answer


jewels, stones = "aA", "aAAbbbb"

solution = Solution()
print(solution.numJewelsInStones(jewels, stones))