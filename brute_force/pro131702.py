'''

https://school.programmers.co.kr/learn/courses/30/lessons/131702
- Programmers 131702 고고학 최고의 발견 (Lv.3)
- Brute Force

'''

from itertools import product
from copy import deepcopy

def solution(clockHands):
    n = len(clockHands)
    answer = float('inf')

    # 윗줄의 경우에 따라 아랫줄의 경우가 정해진다
    # 그래서 첫번째 줄의 모든 경우를 구한 후 시계바늘을 돌려 0이 되도록 한다

    # 첫번째 줄 경우의 수 (중복 순열): 4πn
    for cases in product(range(4), repeat=n):
        copy_clock = deepcopy(clockHands)
        moves = 0

        # 첫 번째 줄 시계바늘 돌리기
        for i in range(n):
            if cases[i] > 0:  # 0이면 돌릴 필요 없음
                turn_clock(cases[i], 0, i, copy_clock)
                moves += cases[i]

        # 나머지 줄 시계바늘 돌리기
        for i in range(1, n):
            for j in range(n):
                if copy_clock[i-1][j] != 0:  # 위 칸이 0이 아닐 경우 돌려야 함
                    turning = (4 - copy_clock[i-1][j]) % 4
                    if turning > 0:  # 0이면 돌릴 필요 없음
                        turn_clock(turning, i, j, copy_clock)
                        moves += turning
        
        # 모든 시계가 0인지 확인 후 최소값 갱신
        if all(all(clock == 0 for clock in row) for row in copy_clock):
            answer = min(answer, moves)

    return answer

# 시계바늘 돌리기
def turn_clock(turning, r, c, clock_hands):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(clock_hands)

    # 현재 위치 돌리기
    clock_hands[r][c] = (clock_hands[r][c] + turning) % 4

    # 현재 기준 상/하/좌/우 돌리기
    for dir in range(4):
        x = c + dx[dir]
        y = r + dy[dir]
        if 0 <= x < n and 0 <= y < n:
            clock_hands[y][x] = (clock_hands[y][x] + turning) % 4

