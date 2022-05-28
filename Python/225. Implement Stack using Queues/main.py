import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class MyStack:
    
    def __init__(self):
        self.queue, self.rQueue = [], []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.queue) - 1):
            self.rQueue.append(self.queue.pop(0))
        result = self.queue.pop(0)

        for _ in range(len(self.rQueue)):
            self.push(self.rQueue.pop(0))

        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        for _ in range(len(self.queue) - 1):
            self.rQueue.append(self.queue.pop(0))

        result = self.queue[0]

        self.rQueue.append(self.queue.pop(0))

        for _ in range(len(self.rQueue)):
            self.push(self.rQueue.pop(0))
            
        return result
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue == []


# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

myStack = MyStack()
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())
print(myStack.pop())
print(myStack.empty())