'''

https://school.programmers.co.kr/learn/courses/30/lessons/133500
- Programmers 133500 등대 (Lv.3)
- DP

'''

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    
    # 그래프 생성
    graph = defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    # DP 배열 (dp[v][0]: v가 꺼져 있을 때 최소 등대 수, dp[v][1]: v가 켜져 있을 때 최소 등대 수)
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        dp[node][1] = 1  # 노드가 켜져 있을 때 기본값 = 1
        
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                dp[node][0] += dp[child][1]  # 내가 꺼져있을 때 자식은 반드시 켜져 있어야 함
                dp[node][1] += min(dp[child][0], dp[child][1])  # 내가 켜져 있을 때 자식은 꺼져도 되고 켜져도 됨
        
    # 트리의 루트는 1번 노드로 가정
    dfs(1)

    return min(dp[1][0], dp[1][1])  # 루트 노드에서 최소 등대 수 반환
