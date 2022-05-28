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
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs=[]
        tempLetterLogs=[]
        digitLogs=[]
        result=[]

        for log in logs:
            identifier=log[:log.index(' ')]
            contents=log[log.index(' ')+1:]
            contents=contents.replace(' ', '')
            
            if contents.isdigit():
                digitLogs.append(log)
            else:
                temp=[]
                temp.append(log[:log.index(' ')])
                temp.append(log[log.index(' ')+1:])
                tempLetterLogs.append(temp)

        # letterLog ordering
        letterLogs=sorted(tempLetterLogs, key=lambda x:x[0])
        letterLogs=sorted(letterLogs, key=lambda x:x[1])
        for log in letterLogs:
            result.append(log[0] + ' ' + log[1])
        
        result+=digitLogs

        return result

# logs=['dig1 8 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero']
# logs=['a1 9 2 3 1','g1 act car','zo4 4 7','ab1 off key dog','a8 act zoo']
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

solution=Solution()
print(solution.reorderLogFiles(logs))