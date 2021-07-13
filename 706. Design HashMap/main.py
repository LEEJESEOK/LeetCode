import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = dict()

        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashMap[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashMap:
            del self.hashMap[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

myHashMap = MyHashMap()
print(myHashMap.put(1, 1))
print(myHashMap.put(2, 2))
print(myHashMap.get(1)   )
print(myHashMap.get(3)   )
print(myHashMap.put(2, 1))
print(myHashMap.get(2)   )
print(myHashMap.remove(2))
print(myHashMap.get(2)   )