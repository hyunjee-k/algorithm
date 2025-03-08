'''

https://www.acmicpc.net/problem/1365
- 백준 1365 꼬인 전깃줄 (골드2)
- binary search

LIS (Longest Increasing Subsequence)

'''

import sys
from bisect import bisect_left

n =  int(sys.stdin.readline())
lights = list(map(int, sys.stdin.readline().split()))

lis = []
cnt = 0
for l in lights:
    idx = bisect_left(lis, l)
    if idx == cnt:
        lis.append(l)
        cnt += 1
    else:
        lis[idx] = l

print(n - cnt)
