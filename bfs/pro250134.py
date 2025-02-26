'''

https://school.programmers.co.kr/learn/courses/30/lessons/250134
- Programmers 250134 수레 움직이기기 (Lv.3)
- BFS

'''

from collections import deque

def solution(maze):
    dq = deque()
    n = len(maze)
    m = len(maze[0])

    # 상, 하, 좌, 우 이동을 위한 배열 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # red, blue 시작 위치 확인
    red = (0,0)
    blue = (0,0)
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red = (i,j)
            elif maze[i][j]== 2:
                blue = (i,j)

    red_visit = set({red})
    blue_visit = set({blue})
    dq.append([red, blue, 0, red_visit, blue_visit])
    while dq:
        red, blue, step, red_visit, blue_visit = dq.popleft()

        # 도착
        if maze[red[0]][red[1]] == 3 and maze[blue[0]][blue[1]] == 4:
            return step

        for i in range(4):
            rx = red[1] + dx[i]
            ry = red[0] + dy[i]

            # (빨강) 도착한 경우 이동하지 않음 
            if maze[red[0]][red[1]] == 3: 
                rx = red[1]
                ry = red[0]
            else: 
                # (빨강) 경계 및 벽 확인
                if out_of_index(maze, ry, rx): continue
                # (빨강) 방문 여부 확인 
                if (ry, rx) in red_visit: continue
            
            for j in range(4):
                bx = blue[1] + dx[j]
                by = blue[0] + dy[j]
                
                # (파랑) 도착한 경우 이동하지 않음 
                if maze[blue[0]][blue[1]] == 4:
                    bx = blue[1]
                    by = blue[0]
                else:
                    # (파랑) 경계 및 벽 확인 
                    if out_of_index(maze, by, bx): continue
                    # (파랑) 방문 여부 확인 
                    if (by, bx) in blue_visit: continue 

                # 교차 이동 불가 
                if ry == blue[0] and rx == blue[1] and by == red[0] and bx == red[1]: continue
                # 동시에 같은 곳으로 이동 불가 
                if rx == bx and ry == by: continue

                # 다음 방문지 deque에 추가 및 방문 체크 
                dq.append([(ry, rx), (by, bx), step+1, red_visit|{(ry,rx)}, blue_visit|{(by,bx)}])
          
    return 0


def out_of_index(maze, r, c):
    if 0 <= r and r < len(maze) and 0 <= c and c < len(maze[0]):
        if maze[r][c] == 5: # 벽인 경우
            return True
        return False
     
    return True

