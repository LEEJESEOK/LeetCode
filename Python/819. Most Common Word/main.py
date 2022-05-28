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
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        paragraph=re.sub("[!?',;.]", ' ', paragraph)

        wordDict={}
        for word in paragraph.split():
            if not word in wordDict:
                wordDict[word]=0
            wordDict[word]+=1
        
        for word in banned:
            if word in wordDict:
                del wordDict[word]


        return max(wordDict, key=wordDict.get)


# paragraph='Bob hit a ball, the hit BALL flew far after it was hit.'
# banned=['hit']
# paragraph = 'a.'
# banned = []
paragraph = "Bob!"
banned = ["hit"]

solution=Solution()
print(solution.mostCommonWord(paragraph, banned))