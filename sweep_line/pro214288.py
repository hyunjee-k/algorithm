'''

https://school.programmers.co.kr/learn/courses/30/lessons/214288
- Programmers 214288 상담원 인원 (Lv.3)
- 정렬과 스위핑

중복순열 product 사용법 익히기기

'''

import heapq
from itertools import product

def solution(k, n, reqs):
    answer = float("inf")
    
    # 상담유형 당 할당 멘토 수를 중복순열로 계산
    for mentor_distribute in product(range(1, n+1), repeat=k):
        if sum(mentor_distribute) == n:
            waiting_time = calc_time(mentor_distribute, k, reqs)
            answer = min(answer, waiting_time)
    
    return answer

def calc_time(mentor_distribute, k, reqs):
    mentor = []
    waiting = 0
    
    for n in mentor_distribute:
        mentor.append([0 for _ in range(n)])
    
    for req_at, take_time, consult_type in reqs:
        time = heapq.heappop(mentor[consult_type-1])
        waiting += max(0, time-req_at)
        heapq.heappush(mentor[consult_type-1], max(req_at, time)+take_time)
    
    return waiting
    