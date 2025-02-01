'''

https://www.acmicpc.net/problem/1504
- 백준 1504 특정한 최단 경로로 (골드4)
- dijkstra

모든 간선이 양수 일 때 최단거리 찾기

'''

import sys
import heapq
from collections import defaultdict

class Dijkstra:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########
        
        # 정점의 개수 n, 간선의 개수 e
        self.n, self.e = map(int, sys.stdin.readline().split()) 
        # 정점 간 비용 정보
        self.graph = defaultdict(list)
        for _ in range(self.e):
            a, b, c = map(int, sys.stdin.readline().split())
            self.graph[a].append((b, c))
            self.graph[b].append((a, c))
        # 꼭 지나야하는 정점 v1, v2
        self.v1, self.v2 = map(int, sys.stdin.readline().split()) 

    def dijkstra(self, start): 
        q = []
        cost = [float('inf') for _ in range(d.n + 1)]

        cost[start] = 0
        heapq.heappush(q, [cost[start], start])
        while q:
            cur_cost, cur_pos = heapq.heappop(q)

            if cost[cur_pos] < cur_cost:
                continue 
        
            for next_pos, next_cost in self.graph[cur_pos]:
                total_cost = next_cost + cur_cost
                if total_cost <= cost[next_pos]:
                    cost[next_pos] = total_cost
                    heapq.heappush(q, [total_cost, next_pos])

        return cost # start 에서 모든 노드까지 최소 비용이 담겨있음음
    


if __name__ == "__main__":
    d = Dijkstra()
    
    # start = 1
    cost_1 = d.dijkstra(1)
    # start = v1
    cost_v1 = d.dijkstra(d.v1)
    # start = v2
    cost_v2 = d.dijkstra(d.v2)

    # 두 경로의 비용 계산
    path1 = cost_1[d.v1] + cost_v1[d.v2] + cost_v2[d.n]
    path2 = cost_1[d.v2] + cost_v2[d.v1] + cost_v1[d.n]

    result = min(path1, path2)
    if result == float('inf'):
        print(-1)
    else: 
        print(result)

