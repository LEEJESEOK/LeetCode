# LeetCode   
LeetCode Algorithm Solutions

# 목차
1. [문자열 조작](#1-문자열-조작)

    1.1 [Valid Palindrome](#11-valid-palindrome-two-pointers-string)

    1.2 [Reverse String](#12-reverse-string-two-pointers-string-recursion)
2. [배열]()
3. [연결 리스트]()
4. [스택, 큐]()
5. [데크, 우선순위 큐]()
6. [해시 테이블]()
7. [그래프]()
8. [최단 경로 문제]()
9. [트리]()


# 1. 문자열 조작   
## 1.1 [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Two Pointers, String)
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.   
주어진 문자열이 팬린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.   
### 1.1.1 리스트로 변환
리스트에 문자열을 저장하고 하나씩 확인
```python
while len(strs) > 1:
    if strs.pop(0) != strs(0):
        return False;

return True
```
### 1.1.2 Deque 적용
```python
while len(strs) > 1:
    if strs.popleft() != strs(0):
        return False;

return True
```
### 1.1.3 슬라이싱 사용
```python
return s == s[::-1]
```

## 1.2 [Reverse String](https://leetcode.com/problems/reverse-string/) (Two Pointers, String, Recursion)
Write a function that reverses a string. The input string is given as an array of characters `s`.   
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배여려이며, 리턴 없이 리스트 내부를 직접 조작하라.
### 1.2.1 투 포인터를 이용한 스왑
```python
left, right = 0, len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
```
   
### 1.2.2 파이썬다운(Pythonic way) 방식
```python
s.reverse()
```
