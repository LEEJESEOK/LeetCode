# LeetCode   
LeetCode Algorithm Solutions

<br>

# 목차
1. [문자열 조작](#1-문자열-조작)   
    1.1 [Valid Palindrome](#11-valid-palindrome-two-pointers-string)   
    1.2 [Reverse String](#12-reverse-string-two-pointers-string-recursion)   
    1.3 [Reorder Data in Log Files](#13-reorder-data-in-log-files-array-string-sorting)   
    1.4 [Most Common Word](#14-most-common-word-hash-table-string)   
    1.5 [Group Anagrams](#15-group-anagrams-hash-table-string-sorting)
2. [배열](#2-배열)   
3. [연결 리스트](#3-연결-리스트)   
4. [스택, 큐](#4-스택,-큐)   
5. [데크, 우선순위 큐](#5-데크,-우선순위-큐)   
6. [해시 테이블](#6.-해시-테이블)   
7. [그래프](#7.-그래프)   
8. [최단 경로 문제](#8.-최단-경로-문제)   
9. [트리](#9.-트리)   
10. [힙]()   
11. [트라이]()   
12. [정렬]()   
13. [이진 검색]()   
14. [비트 조작]()   
15. [슬라이딩 윈도우]()   
16. [그리디 알고리즘]()   
17. [분할 정복]()   
18. [다이나믹 프로그래밍]()   

<br>

# 1. 문자열 조작   
## 1.1 [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Two Pointers, String)   
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.   
주어진 문자열이 팬린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.   

<br>

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
    if strs.popleft()    != strs(0):
        return False;

return True
```
### 1.1.3 슬라이싱 사용
```python
return s == s[::-1]
```

<br>

## 1.2 [Reverse String](https://leetcode.com/problems/reverse-string/) (Two Pointers, String, Recursion)   
Write a function that reverses a string. The input string is given as an array of characters `s`.   
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배여려이며, 리턴 없이 리스트 내부를 직접 조작하라.   

<br>

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

<br>

## 1.3 [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/) (Array, String, Sorting)   
You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the <b>identifier</b>.   

>There are two types of logs:   
>- <b>Letter-logs</b>: All words (except the identifier) consist of lowercase English letters.   
>- <b>Digit-logs</b>: All words (except the identifier) consist of digits.   
> 
> Reorder these logs so that:   
>1. The <b>letter-logs</b> come before all <b>digit-logs</b>.
>2. The <b>letter-logs</b> are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
>3. The <b>digit-logs</b> maintain their relative ordering.   
>
>Return the <i>final order</i> of the logs.   

로그를 재정렬하라. 기준은 다음과 같다.   
>1. 로그의 가장 앞 부분은 식별자다.   
>2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.   
>3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.   
>4. 숫자 로그는 입력 순서대로 한다.   

<br>

### 1.3.1 람다와 +연산자를 사용   
`isdigit()`을 이용하여 숫자인지 판별   
```python
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
```
식별자를 제외한 문자열 `[1:]`을 키로 하여 정렬하며, 동일한 경우 후순위로 식별자 `[0]`를 이용하여 정렬한다.

```python
letters, digits = [], []
for log in logs:
    if log.split()[1],isdigit():
        digits.apeend(log)
    else:
        letters.apeend(log)

letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
return letters + digits
```

<br>

## 1.4 [Most Common Word](https://leetcode.com/problems/most-common-word/) (Hash Table, String)   
The words in `paragraph` are <b>case-insensitive</b> and the answer should be returned in <b>lowercase</b>.   
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.   

<br>

### 1.4.1 리스트 컴프리헨션, Counter 객체 사용
정규식을 사용하여 정규화
`\w` : 단어 문자(Word Character)   
`^` : not   
아래 코드의 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.

```python
words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]

counts = collections.Counter(words)
# 가장 흔하게 등장하는 순으로 정렬, 첫번째 인덱스 반환
return counts.most_common(1)[0][0]
```

<br>

## 1.5 [Group Anagrams](https://leetcode.com/problems/group-anagrams/)(Hash Table, String, Sorting)
Given an array of strings `strs`, group the <b>anagrams</b> together. You can return the answer in <b>any order</b>.   

An <b>Anagram</b> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.   
문자열 배열을 받아 애너그램 단위로 그룹핑하라.   

<br>

### 1.5.1 정렬하여 딕셔너리에 추가
애너그램인 단어는 정렬하면 같은 값을 갖는 특징이 있다.   
`defaultdict()`는 항상 디폴트를 생성해서 `KeyError`가 발생하지 않는다.

```python
anagrams = collections.defaultdict(list)

for word in strs:
    # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)

return anagrams.values()
```

- 여러가지 정렬 방법
```python
>>> a = [2, 5, 1, 9, 7]
>>> sorted(a)
[1, 2, 5, 7, 9]
```
```python
>>> a = 'zbdaf'
>>> sorted(a)
['a', 'b', 'd', 'f', 'z']
```
```python
>>> b = 'zbdaf'
>>> "".join(sorted(b))
'abdfz'
```
`sort()` : 제자리 정렬, 정렬 결과를 별도로 리턴하는 `sorted()`와는 다르다.
```python
alist.sort()            # sort()는 리스트 자체를 제자리 정렬
alist = blist.sort()    # 잘못된 구문
                        # sort() 함수는 None을 리턴하므로 주의 필요
```
`sorted()`는 `key=`옵션을 지정해 정렬을 위한 키 또는 함수를 별도로 지정할 수 있다.   
```python
>>> c = ['ccc', 'aaaa', 'd', 'bb']
>>> sorted(c, key=len)
['d', 'bb', 'ccc', 'aaaa']
```
이 경우 문자열의 알파벳 순서가 아닌 길이 순서로 정렬된다.


<br>

## 1.6 

<br>

# 2. 배열

<br>

# 3. 연결 리스트

<br>

# 4. 스택, 큐

<br>

# 5. 데크, 우선순위 큐

<br>

# 6. 해시 테이블

<br>

# 7. 그래프

<br>

# 8. 최단 경로 문제

<br>

# 9. 트리

<br>

