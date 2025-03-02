'''

https://school.programmers.co.kr/learn/courses/30/lessons/138476
- Programmers 138476 귤 고르기 (Lv.2)
- greedy

'''

import heapq
from collections import defaultdict

def solution(k, tangerine):

    kind_of = defaultdict(int)
    for t in tangerine:
        kind_of[t] += 1
    
    hq = []
    for _, val in kind_of.items():
        heapq.heappush(hq, -val)

    print(hq)
    
    total = 0
    answer = 0
    while hq:
        t = heapq.heappop(hq)
        answer += 1
        total -= t
        print(answer, t, total, k)
        if total >= k:   
            break

    return answer
