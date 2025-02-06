'''

https://school.programmers.co.kr/learn/courses/30/lessons/1844
- Programmers 1844 게임 맵 최단거리 (Lv.2)
- BFS

DFS 로 풀면 시간초과 발생

'''

import sys
from collections import deque
sys.setrecursionlimit(10000)

# 하우좌상 탐색
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
# map 크기
n = 0
m = 0

def solution(maps):
    global n, m
    n = len(maps[0])
    m = len(maps)
    
    answer = bfs(maps)

    return answer

def bfs(maps):
    global n, m, dx, dy

    dq = deque()
    visit = [[-1] * n for _ in range(m)] 

    dq.append((0,0))
    visit[0][0] = 1
    while dq:
        x, y = dq.popleft()
        if x == n - 1 and y == m - 1: 
            return visit[m-1][n-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if out_of_index(nx, ny): continue
            if maps[ny][nx] and visit[ny][nx] == -1:
               visit[ny][nx] = visit[y][x] + 1
               dq.append((nx, ny))
    
    return -1

def out_of_index(x, y):
    global n, m
    if x < 0 or x >= n: return True
    if y < 0 or y >= m: return True
    return False

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
result = solution(maps)
print(result)