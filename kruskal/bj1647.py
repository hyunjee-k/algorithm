'''

https://www.acmicpc.net/problem/1647
- 백준 1647 도시 분할 계획 (골드4)
- Kruskal

Kruskal은 최소 비용으로 모든 노드를 연결할 때 사용
UnionFind를 이용해 풀 수 있음
간선의 비용을 오름차순으로 정렬 필요

'''

import sys
sys.setrecursionlimit(10000) # 재귀 허용 깊이 임의로 지정

class Kruskal:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 첫 줄: 집의 개수 N, 길의 개수 M
        self.n, self.m = map(int, sys.stdin.readline().split())

        # 연결 비용 정보: A, B 집과 그 둘의 연결비용 C
        self.costs = [list(map(int, sys.stdin.readline().split())) for _ in range(self.m)]

        ##########
        # 초기화 #
        ##########

        self.root = [i for i in range(self.n + 1)]
        self.size = [1] * (self.n + 1)

    
    def find(self, idx):
        if self.root[idx] != idx:
            self.root[idx] = self.find(self.root[idx])

        return self.root[idx]
    
    def union(self, root_x, root_y):
        # size 기반으로 유니온 수행
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.root[root_y] = root_x
            self.size[root_x] += self.size[root_y]


if __name__ == "__main__":
    k = Kruskal()

    # 집이 총 2개인 경우 예외처리
    if k.n == 2: 
        print(0)
        exit(0)

    # 비용을 기준으로 오름차순 정렬
    k.costs.sort(key=lambda c:c[2])

    # 최소 스패닝 트리 구성
    answer = 0
    max_cost = -1
    for a, b, cost in k.costs:
        root_a = k.find(a)
        root_b = k.find(b)
        if root_a != root_b:
            k.union(root_a, root_b)
            answer += cost
            max_cost = max(cost, max_cost)

    # 가장 큰 간선 비용을 빼서 두 마을로 분리
    print(answer - max_cost)
