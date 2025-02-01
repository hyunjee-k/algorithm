'''

https://www.acmicpc.net/problem/11657
- 백준 11657 타임머신 (골드4)
- Bellman-Ford

'''

import sys

class BellmanFord:
    def __init__(self):
        # 도시의 수 n, 버스 노선의 수 m
        self.n, self.m = map(int, sys.stdin.readline().split())
        # 버스 노선의 정보
        self.route = []
        for _ in range(self.m):
            temp = list(map(int, sys.stdin.readline().split()))
            self.route.append(temp)
        
        # 초기화
        self.distance = [float('inf') for _ in range(self.n + 1)]

    def bellman_ford(self, start):
        self.distance[start] = 0

        # find shortest path (start-to-all)
        for _ in range(self.n - 1):
            for a, b, cost in self.route:
                if self.distance[a] + cost < self.distance[b]:
                    self.distance[b] = self.distance[a] + cost

        # check negative cycle        
        for a, b, cost in self.route:
            if self.distance[a] + cost < self.distance[b]:
                return True

        return False



if __name__ == "__main__":
    bf = BellmanFord()

    if bf.bellman_ford(1): print(-1) 
    else:
        for i in range(2, bf.n + 1):
            if bf.distance[i] == float('inf'): print(-1)
            else: print(bf.distance[i])