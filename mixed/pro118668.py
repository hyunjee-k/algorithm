'''

https://school.programmers.co.kr/learn/courses/30/lessons/118668
- Programmers 118668 코딩 테스트 공부 (Lv.3)
- dp + dijkstra

- 최소 시간으로 모든 문제까지 도달하기 
- 최소 시간은 dp 형식으로 저장해두기기
- 시간 단축을 위해 다익스트라 필요

'''

import heapq

def solution(alp, cop, problems):
    # 문제를 풀기 위해 필요한 최소 알고력, 코딩력 계산
    max_alp = max(alp, max(p[0] for p in problems))
    max_cop = max(cop, max(p[1] for p in problems))

    # dp[알고력][코딩력] = 최단 시간
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0  # 초기 상태는 주어진 알고력, 코딩력에서 시간 0

    ''' dijkstra '''
    hq = [(0, alp, cop)] # 시간, 알고력, 코딩력
    while hq:
        time, cur_alp, cur_cop = heapq.heappop(hq)

        # 목표 달성
        if cur_alp >= max_alp and cur_cop >= max_cop: return time

        # 알고력, 코딩력 증가 시키기
        # 방법1: 알고력++
        if cur_alp + 1 <= max_alp: # 배열 범위 확인
            if time + 1 < dp[cur_alp+1][cur_cop]:
                dp[cur_alp+1][cur_cop] = time + 1
                heapq.heappush(hq, (time+1, cur_alp+1, cur_cop))
            
        # 방법2: 코딩력++
        if cur_cop + 1 <= max_cop: # 배열 범위 확인
            if time + 1 < dp[cur_alp][cur_cop+1]:
                dp[cur_alp][cur_cop+1] = time + 1
                heapq.heappush(hq, (time+1, cur_alp, cur_cop+1))
        
        # 방법3: 문제 풀기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if cur_alp < alp_req or cur_cop < cop_req: continue
            
            new_alp = min(cur_alp + alp_rwd, max_alp)
            new_cop = min(cur_cop + cop_rwd, max_cop)
            if time + cost < dp[new_alp][new_cop]:
                dp[new_alp][new_cop] = time + cost
                heapq.heappush(hq, (time + cost, new_alp, new_cop))

    return -1 


alp = 0
cop = 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

answer = solution(alp, cop, problems)
print(answer)