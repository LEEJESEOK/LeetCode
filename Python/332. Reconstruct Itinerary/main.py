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
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = DefaultDict(list)

        tickets.sort(key = lambda x:x[1])

        for u, v in tickets:
            graph[u].append(v)

        itinerary, stack = [], ["JFK"]

        while stack:
            curr = stack[-1]

            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop(0))
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
# tickets = [["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]
solution = Solution()
print(solution.findItinerary(tickets))
