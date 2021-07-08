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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))