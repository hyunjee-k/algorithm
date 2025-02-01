'''

https://www.acmicpc.net/problem/1916
- 백준 1916 최소비용 구하기 (골드5)
- dijkstra

모든 간선이 양수 일 때 최단거리 찾기

'''

import sys
import heapq

class Dijkstra:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 도시의 개수 n
        self.n = int(sys.stdin.readline())
        # 버스의 개수 m
        self.m = int(sys.stdin.readline())
        # 도시간 비용 정보: 출발지/도착지/비용 (단방향)
        self.graph = [[float('inf') for _ in range(self.n+1)] for _ in range(self.n+1)]
        for _ in range(self.m):
            a, b, c = map(int, sys.stdin.readline().split())
            self.graph[a][b] = min(self.graph[a][b], c) # 동일한 경로가 여러번 입력될 수 있음
        # 출발지와 도착지
        self.start, self.end = map(int, sys.stdin.readline().split())
        

    def dijkstra(self):
        q = []
        cost = [float('inf') for _ in range(self.n + 1)]

        cost[self.start] = 0
        heapq.heappush(q, [cost[self.start], self.start])
        while q:
            cur_cost, cur_pos = heapq.heappop(q)
            
            if cur_pos == self.end: # 목적지에 도착한 경우 stop
                break

            if cost[cur_pos] < cur_cost: # 기존 비용보다 크면 skip
                continue

            for next_pos, next_cost in enumerate(self.graph[cur_pos]):
                total_cost = cur_cost + next_cost
                if total_cost < cost[next_pos]: # 기존 비용보다 작으면 비용 갱신 후 탐색
                    cost[next_pos] = total_cost
                    heapq.heappush(q, [total_cost, next_pos])
            
        return cost[self.end]    



if __name__ == "__main__":
    d = Dijkstra()
    print(d.dijkstra())
