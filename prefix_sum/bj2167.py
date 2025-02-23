'''

https://www.acmicpc.net/problem/2167
- 백준 2167 2차원 배열의 합 (실버5)
- 구간 합 

'''

import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

k = int(sys.stdin.readline())

dir = []
for i in range(k):
    dir.append(list(map(int, sys.stdin.readline().split())))

# 누적합 구하기
prefix_sum = [[0 for _ in range(m+1)]]
for a in arr: 
    prefix_sum.append([0] + a[:])

# 1. 행 단위 누적합
for i in range(n+1):
    for j in range(m):
        prefix_sum[i][j+1] += prefix_sum[i][j]

# 2. 열 단위 누적합
for i in range(n):
    for j in range(m+1):
        prefix_sum[i+1][j] += prefix_sum[i][j]

for i in prefix_sum:
    print(i)

# 구하려는 범위의 누적합 출력
for r1, c1, r2, c2 in dir:
    print(prefix_sum[r2][c2], prefix_sum[r2][c1-1], prefix_sum[r1-1][c2], prefix_sum[r1][c1])
    res = prefix_sum[r2][c2] - prefix_sum[r2][c1-1] - prefix_sum[r1-1][c2] + prefix_sum[r1-1][c1-1]
    print(res)