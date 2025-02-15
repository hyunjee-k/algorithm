'''

https://www.acmicpc.net/problem/12851
- 백준 12851 숨바꼭질2 (골드4)
- BFS

'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs():
    if n == k: return 0, 1

    time = float('inf')
    cnt = 0
    visit = [float('inf') for _ in range(max(n, k)*2 + 1)]

    dq = deque()
    dq.append(n)
    visit[n] = 0
    while dq:
        x = dq.popleft()

        if visit[x] > time: continue

        if x == k:
            if visit[x] < time: 
                time = visit[x]
                cnt = 1
            elif visit[x] == time: cnt += 1
            else: continue

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max(n, k) * 2: # 배열 범위 확인
                if visit[nx] >= visit[x] + 1:
                    dq.append(nx)
                    visit[nx] = visit[x] + 1

    return time, cnt


time, cnt = bfs()
print(time)
print(cnt)