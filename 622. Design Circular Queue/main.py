import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class MyCircularQueue:
    
    def __init__(self, k: int):
        self.front, self.rear = 0, 0
        self.size = k + 1
        self.queue = [-1] * (self.size)

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[(self.front + 1) % self.size] = -1
            self.front = (self.front + 1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[(self.front + 1) % self.size]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# myCircularQueue = MyCircularQueue(3)
# print(myCircularQueue.enQueue(1))
# print(myCircularQueue.enQueue(2))
# print(myCircularQueue.enQueue(3))
# print(myCircularQueue.enQueue(4))
# print(myCircularQueue.Rear())
# print(myCircularQueue.isFull())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.enQueue(4))
# print(myCircularQueue.Rear())
# myCircularQueue = MyCircularQueue(6)
# print(myCircularQueue.enQueue(6))
# print(myCircularQueue.Rear())
# print(myCircularQueue.Rear())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.enQueue(5))
# print(myCircularQueue.Rear())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.Front())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.deQueue())


myCircularQueue = MyCircularQueue(2)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(3))
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(3))
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(3))
print(myCircularQueue.deQueue())
print(myCircularQueue.Front())