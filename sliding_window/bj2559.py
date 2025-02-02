'''

https://www.acmicpc.net/problem/2559
- 백준 2559 수열 (실버3)
- Sliding Window

'''

import sys

n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

max_sum = sum(temp[:k])
prev_sum = max_sum
for i in range(k, len(temp)):
    prev_sum = prev_sum + temp[i] - temp[i-k]
    max_sum = max(max_sum, prev_sum)

print(max_sum)