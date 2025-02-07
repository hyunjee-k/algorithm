'''

https://school.programmers.co.kr/learn/courses/30/lessons/150367
- Programmers 150367 표현 가능한 이진트리 (Lv.3)
- DFS

'''

from collections import deque

def solution(numbers):
    answer = []

    for num in numbers:
        binary = make_binary(num)
        answer.append(make_tree(binary))

    return answer


def make_binary(number):
    binary = deque()
    s = number
    while s > 0:
        r = s % 2  
        s //= 2
        binary.appendleft(r)

    return binary


def make_tree(binary):
    n = len(binary)

    # 포화 이진트리로 만들기
    ### 트리 높이: x
    ### 노드 개수: 2**(x+1) - 1 
    level = 0
    while True:
        if n > 2**(level+1) - 1: 
            level += 1
            continue
        else: break
    
    for _ in range((2**(level+1)-1) - n):
        binary.appendleft(0)
        n+=1

    binary = list(binary)
    
    # 노드 개수 1이면 탐색 안함
    if n == 1: return 1

    parent = True
    if binary[n//2] == 0: parent = False
    if not dfs(parent, binary[:n//2]): return 0
    if dfs(parent, binary[n//2+1:]): return 1

    return 0


def dfs(parent, arr):
    n = len(arr)

    # 조상 중 0이 있는데 자식이 1이면 탐색 중단
    if not parent and arr[n//2] == 1:
        return False
    
    if arr[n//2] == 0:
        parent = False
    
    if n//2 > 0:
        if not dfs(parent, arr[:n//2]): return False
        return dfs(parent, arr[n//2+1:])
    
    return True
