'''

https://www.acmicpc.net/problem/13549
- 백준 13549 숨바꼭질 3 (골드5)
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
        
        # 수빈이의 위치 n, 동생의 위치 k
        self.n, self.k = map(int, sys.stdin.readline().split())
        self.max_pos = max(self.n, self.k)

    def dijkstra(self):
        q = []
        cost = [float('inf') for _ in range(self.max_pos*2 + 1)]
        
        cost[self.n] = 0
        heapq.heappush(q, (cost[self.n], self.n))
        while q:
            cur_cost, cur_pos = heapq.heappop(q)

            if cur_pos == self.k:
                break

            if cost[cur_pos] < cur_cost:
                continue

            # x * 2
            if cur_pos * 2 <= self.max_pos * 2 and cur_cost < cost[cur_pos * 2]:
                cost[cur_pos * 2] = cur_cost
                heapq.heappush(q, (cur_cost, cur_pos * 2))

            # x + 1
            if cur_pos + 1 <= self.max_pos * 2 and cur_cost + 1 < cost[cur_pos + 1]:
                cost[cur_pos + 1] = cur_cost + 1
                heapq.heappush(q, (cur_cost + 1, cur_pos + 1))

            # x - 1
            if cur_pos - 1 >= 0 and cur_cost + 1 < cost[cur_pos - 1]:
                cost[cur_pos - 1] = cur_cost + 1
                heapq.heappush(q, (cur_cost + 1, cur_pos - 1))

        return cost[self.k]
    


if __name__ == "__main__":
    d = Dijkstra()
    print(d.dijkstra())