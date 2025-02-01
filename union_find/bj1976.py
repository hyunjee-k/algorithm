'''

https://www.acmicpc.net/problem/1976
- 백준 1976 여행가자자 (골드4)
- Union-Find

여러번 방문 가능하며 방문 가능 여부를 물었으므로 union-find
연결된 도시들끼리 합치고 여행 경로를 돌면서 같은 집합인지 확인
N이 200이므로 시간초과 나지 않음

'''

import sys
sys.setrecursionlimit(10000) # 재귀 허용 깊이 임의로 지정

class DisjointSet:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 첫 줄: 총 도시시 수 N
        self.n = int(sys.stdin.readline())
        
        # 두 번째 줄: 여행할 도시 수 M
        self.m = int(sys.stdin.readline())
        
        # 도시 연결 정보
        self.cities = [list(map(int, sys.stdin.readline().split())) for _ in range(self.n)]

        # 여행 계획
        self.route = list(map(int, sys.stdin.readline().split()))

        ##########
        # 초기화 #
        ##########

        self.parent = [ i for i in range(self.n)]


    def find(self, idx):
        if self.parent[idx] == idx:
            return idx
        
        self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]
    

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return
        
        if parent_x < parent_y:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y

        return


if __name__ == "__main__":
    ds = DisjointSet()

    for i in range(ds.n):
        for j in range(ds.n):
            if ds.cities[i][j]:  # 두 도시가 연결된 경우
                ds.union(i, j)

    # 여행 계획의 모든 도시가 같은 루트에 속하는지 확인
    root = ds.find(ds.route[0] - 1)
    for i in ds.route[1:]:
        if ds.find(i - 1) != root:
            print('NO')
            exit(0)

    print('YES')
