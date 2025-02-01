'''

https://www.acmicpc.net/problem/30221
- 백준 30221 Brightline - Back to the Future (골드4)
- SPFA(Bellman-Ford)

'''

import sys
from collections import defaultdict, deque

class SPFA:
    def __init__(self):
        input = sys.stdin.read
        data = input().splitlines()
        
        self.n, self.m = map(int, data[0].split())
        self.graph = defaultdict(list)
        
        # 그래프 구축
        for i in range(1, self.m + 1):
            s, e, t, a = data[i].split()
            s, e, a = int(s), int(e), int(a)
            cost = -a if t == 'r' else a
            self.graph[s].append((e, cost))
        
        self.distance = [float('inf')] * (self.n + 1)
        self.in_queue = [False] * (self.n + 1)

    def spfa(self, start):
        # 모든 간선을 반복 탐색하는 대신 거리 갱신이 가능한 정점만 탐색하도록 큐를 사용한 최적화 적용
        queue = deque([start])
        self.distance[start] = 0
        self.in_queue[start] = True

        while queue:
            current = queue.popleft()
            self.in_queue[current] = False

            for neighbor, cost in self.graph[current]:
                if self.distance[current] + cost < self.distance[neighbor]:
                    self.distance[neighbor] = self.distance[current] + cost
                    if not self.in_queue[neighbor]:
                        queue.append(neighbor)
                        self.in_queue[neighbor] = True

    def get_result(self):
        base_time = self.distance[1]
        return sorted(i for i in range(2, self.n + 1) if self.distance[i] < base_time)



if __name__ == "__main__":
    s = SPFA()
    s.spfa(1)
    result = s.get_result()
    if result:
        print(*result)

            