'''

https://www.acmicpc.net/problem/20002
- 백준 20002 사과나무 (골드5)
- 구간 합 

'''

import sys 

n = int(sys.stdin.readline())
profit = []
for i in range(n):
    profit.append(list(map(int, sys.stdin.readline().split())))

prefix_sum = [[0 for _ in range(n+1)]]
for i in profit:
    prefix_sum.append([0] + i[:])

for i in range(n+1):
    for j in range(n):
        prefix_sum[i][j+1] += prefix_sum[i][j]

for i in range(n):
    for j in range(n+1):
        prefix_sum[i+1][j] += prefix_sum[i][j]

max_profit = float('-inf')

 # 모든 K에 대해 탐색 (1 ≤ K ≤ N)
for k in range(1, n + 1):
    for i in range(k, n + 1):  # (i, j): KxK 정사각형의 우측 하단 좌표
        for j in range(k, n + 1):
            total = (prefix_sum[i][j] 
                        - prefix_sum[i - k][j] 
                        - prefix_sum[i][j - k] 
                        + prefix_sum[i - k][j - k])
            max_profit = max(max_profit, total)


print(max_profit)