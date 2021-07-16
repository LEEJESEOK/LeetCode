# using common module in LeetCode
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
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:

        # def dfs(index, sub):
        #     if len(sub) == len(digits):
        #         result.append(sub)
        #         return

        #     for i in range(index, len(digits)):
        #         for j in self.letters[digits[i]]:
        #             dfs((i + 1), (sub + j))

        #     return

        # if digits == "":
        #     return

        # result = []

        # dfs(0, "")

        # return result

        result = []

        for digit in digits:
            if result == []:
                for letter in self.letters[digit]:
                    result.append(letter)
            else:
                sectionLen = len(result)
                result = result * len(self.letters[digit])

                for i in range(len(self.letters[digit])):
                    for j in range(sectionLen * i, sectionLen * (i + 1)):
                        result[j] += self.letters[digit][i]

        return result


digits = "23"
solution = Solution()
print(solution.letterCombinations(digits))
