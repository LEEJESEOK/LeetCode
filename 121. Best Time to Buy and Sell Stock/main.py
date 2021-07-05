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
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        # for i in range(0, len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         temp = prices[j] - prices[i]
        #         if temp > maxProfit :
        #             maxProfit=temp
        
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit


# prices = [7,1,5,3,6,4]
prices = [2,4,1]

solution = Solution()
print(solution.maxProfit(prices))