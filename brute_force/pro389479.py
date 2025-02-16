'''

https://school.programmers.co.kr/learn/courses/30/lessons/389479
- Programmers 389479 서버 증설 횟수 (Lv.2)
- Brute Force

'''

from collections import deque

def solution(players, m, k):

    server_down = deque()
    running = 0
    answer = 0
    for i in range(len(players)):
        # 종료되는 서버가 있는지 확인
        if 0 < len(server_down) and server_down[0][0] == i:
            running -= server_down[0][1]
            server_down.popleft()
        
        # 필요한 서버 수 
        need = players[i] // m

        # 증설이 필요한 경우 
        if running < need:
            add = need - running
            server_down.append([i+k, add])
            answer += add 
            running += add

    return answer
