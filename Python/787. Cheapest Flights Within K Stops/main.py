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


# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for u, v, w in flights:
#             graph[u].append((v, w))

#         # q: [(cost, node, step)]
#         q = [(0, src, k)]

#         while q:
#             price, node, step = heapq.heappop(q)
#             if node == dst:
#                 return price
#             if step >= 0:
#                 for v, w in graph[node]:
#                     alt = price + w
#                     heapq.heappush(q, (alt, v, step - 1))

#         return -1


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costTable = [float('inf') for _ in range(n)]

        # 출발지는 비용이 0
        costTable[src] = 0

        # 0번 갈아탈때 테이블 갱신
        for start, end, cost in flights:
            if start == src:
                costTable[end] = cost

        # k번 갈아탈 동안 반복하기
        for _ in range(0, k):
            # 현재 테이블 복사
            nowCost = costTable[:]

            # 최소값 갱신
            for start, end, cost in flights:
                nowCost[end] = min(nowCost[end], costTable[start] + cost)

            # 테이블 업데이트
            costTable = nowCost

        # 도달하지 못했으면 -1 반환
        if costTable[dst] == float('inf'):
            return -1
        # 도달했다면 코스트 반환
        else:
            return costTable[dst]


solution = Solution()
# print(solution.findCheapestPrice(n=3, flights=[
#       [0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))

# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0
# dst = 2
# k = 0
# print(solution.findCheapestPrice(n, flights, src, dst, k))

n = 4
flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src = 0
dst = 3
k = 1
print(solution.findCheapestPrice(n, flights, src, dst, k))

n = 13
flights = [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [
    2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]]
src = 10
dst = 1
k = 10
