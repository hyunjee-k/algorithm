'''

https://www.acmicpc.net/problem/2665
- 백준 2665 미로만들기 (골드4)
- 1-0 BFS

'''

import sys
import heapq

class BFS:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 방의 수 n
        self.n = int(sys.stdin.readline())
        # 방 정보 
        self.room = []
        for _ in range(self.n):
            temp = list(map(int, sys.stdin.readline().rstrip())) 
            self.room.append(temp)

        ##########
        # 초기화 #
        ##########

        # '상하좌우' 로 이동하기 위한 좌표
        self.dx = [0, 0, -1, 1]
        self.dy = [-1, 1, 0, 0]

    def check_border(self, x, y):
        if x < 0 or x >= self.n: return False
        if y < 0 or y >= self.n: return False
        return True 

    def bfs(self):        
        # 우선순위 큐 초기화
        pq = []
        heapq.heappush(pq, (0, 0, 0))  # (변경 횟수, x, y)

        # 방문 배열 (최소 변경 횟수를 저장)
        visit = [[float('inf')] * self.n for _ in range(self.n)]
        visit[0][0] = 0

        while pq:
            cur_changes, x, y = heapq.heappop(pq)

            # 현재 위치가 도착지인 경우 최소 변경 횟수를 반환
            if x == self.n - 1 and y == self.n - 1:
                return cur_changes

            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]

                if not self.check_border(nx, ny):  # 배열의 범위를 벗어난 경우
                    continue

                # 흰 방인 경우(그대로 이동)
                if self.room[ny][nx] == 1:
                    if cur_changes < visit[ny][nx]:
                        visit[ny][nx] = cur_changes
                        heapq.heappush(pq, (cur_changes, nx, ny))
                # 검은 방인 경우(방을 흰 방으로 변경)
                else:
                    if cur_changes + 1 < visit[ny][nx]:
                        visit[ny][nx] = cur_changes + 1
                        heapq.heappush(pq, (cur_changes + 1, nx, ny))

        return visit[self.n - 1][self.n - 1]


if __name__ == "__main__":
    bfs = BFS()

    print(bfs.bfs())

