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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for word in strs:
            temp=''.join(sorted(word))

            if len(result)==0:
                result.append([temp])
                result.append([word])

            else:
                if not temp in result[0]:
                    result[0].append(temp)
                    result.append([word])
                else:
                    result[result[0].index(temp)+1].append(word)

        del result[0]

        return result


# strs = ['eat','tea','tan','ate','nat','bat']
# strs = [""]
strs = ["a"]

solution = Solution()
print(solution.groupAnagrams(strs))
