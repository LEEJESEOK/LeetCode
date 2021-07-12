import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class MyCircularDeque:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front, self.rear = 0, 0
        self.size = k + 1
        self.deque = [-1]*self.size
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.deque[self.front] = value
            self.front = (self.front - 1 + self.size) % self.size
            return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.deque[self.rear] = value
            return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.deque[(self.front + 1) % self.size] = -1
            self.front = (self.front + 1) % self.size
            return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.deque[self.rear] = -1
            self.rear = (self.rear - 1 + self.size) % self.size
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[(self.front + 1) % self.size]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.size == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# circularDeque = MyCircularDeque(3)
# print(circularDeque.insertLast(1))
# print(circularDeque.insertLast(2))
# print(circularDeque.insertFront(3))
# print(circularDeque.insertFront(4))
# print(circularDeque.getRear())
# print(circularDeque.isFull())
# print(circularDeque.deleteLast())
# print(circularDeque.insertFront(4))
# print(circularDeque.getFront())

# circularDeque = MyCircularDeque(8)
# print(circularDeque.insertFront(5))
# print(circularDeque.getFront())
# print(circularDeque.isEmpty())
# print(circularDeque.deleteFront())
# print(circularDeque.insertLast(3))
# print(circularDeque.getRear())
# print(circularDeque.insertLast(7))
# print(circularDeque.insertFront(7))
# print(circularDeque.deleteLast())
# print(circularDeque.insertLast(4))
# print(circularDeque.isEmpty())

["MyCircularDeque","insertFront","insertLast","getFront","insertLast","getFront","insertFront","getRear","getFront","getFront","deleteLast","getRear"]
[[5],[7],[0],[],[3],[],[9],[],[],[],[],[]]
circularDeque = MyCircularDeque(5)
print(circularDeque.insertFront(7))
print(circularDeque.insertLast(0))
print(circularDeque.getFront())
print(circularDeque.insertLast(3))
print(circularDeque.getFront())
print(circularDeque.insertFront(9))
print(circularDeque.getRear())
print(circularDeque.getFront())
print(circularDeque.getFront())
print(circularDeque.deleteLast())
print(circularDeque.getRear())