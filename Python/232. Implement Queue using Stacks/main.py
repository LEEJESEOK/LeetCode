import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        rStack = []
        for _ in range(len(self.stack) - 1):
            rStack.append(self.stack.pop())
        result = self.stack.pop()

        for _ in range(len(rStack)):
            self.stack.append(rStack.pop())

        return result
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        rStack = []
        for _ in range(len(self.stack)):
            rStack.append(self.stack.pop())

        result = rStack[-1]

        for _ in range(len(rStack)):
            self.stack.append(rStack.pop())
        return result
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack == []