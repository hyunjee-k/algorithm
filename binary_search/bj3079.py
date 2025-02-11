'''

https://www.acmicpc.net/problem/3079
- 백준 3079 입국심사 (골드5)
- binary search

'''

import sys 
import heapq

n, m = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(n)]
times.sort()

def check(mid):
    return sum(mid // t for t in times) >= m

def binary_search():
    left = times[0]
    right = times[0] * m
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid    
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
    

print(binary_search())

