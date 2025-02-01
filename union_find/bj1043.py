'''

https://www.acmicpc.net/problem/1043
- 백준 1043 거짓말 (골드4)
- Union-Find

동일 파티에 참석하는 사람을 Union
만약 Union 하려는 대상 중 진실을 알고 있으면 parent 처리
두 대상이 모두 사실을 알면 연결하지 않음
각 파티에 참여하는 사람 중 parent 가 진실을 알고 있는 사람 목록에 있다면 거짓말 불가  

'''

import sys
sys.setrecursionlimit(10000) # 재귀 허용 깊이 임의로 지정

class DisjointSet:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 첫 줄: 사람 수 N, 파티 수 M
        self.n, self.m = map(int, sys.stdin.readline().split())
        
        # 두 번째 줄: 진실을 아는 사람 수와 번호
        truth_input = list(map(int, sys.stdin.readline().split()))
        self.truth_count = truth_input[0]
        self.truth_people = truth_input[1:] if self.truth_count > 0 else []
        
        # 파티 정보 저장
        self.parties = []
        for _ in range(self.m):
            party_input = list(map(int, sys.stdin.readline().split()))
            self.parties.append(party_input[1:])  # 첫 번째 값은 사람의 수, 생략

        ##########
        # 초기화 #
        ##########

        self.parent = [ i for i in range(self.n + 1)]



    def find(self, idx):
        if self.parent[idx] != idx:
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

    if ds.truth_count == 0: # 진실을 아는 사람이 없는 경우 예외 처리
        print(ds.m)
    else: 
        # 진실을 아는 사람들 연결
        root_truth = ds.truth_people[0]
        for person  in ds.truth_people:
            ds.union(root_truth, person)

        # 파티 참석한 사람들 연결
        for party in ds.parties:
            root_person = party[0]
            for person in party[1:]:
                ds.union(root_person, person)
        
        # 거짓말 가능 여부 판단
        answer = 0
        for party in ds.parties:
            if any(ds.find(person) == ds.find(ds.truth_people[0]) for person in party):
                continue
            answer += 1

        print(answer)

        