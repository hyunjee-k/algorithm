'''

https://school.programmers.co.kr/learn/courses/30/lessons/43164
- Programmers 43164 여행경로 (Lv.3)
- DFS

'''

import sys
from collections import  defaultdict
sys.setrecursionlimit(20000)

def solution(tickets):
    # 데이터 정리
    travel_map = defaultdict(list)
    used = defaultdict(list)

    for src, dest in tickets:
        travel_map[src].append(dest)
    
    # 알파벳 순서로 방문할 수 있도록 정렬
    for src in travel_map:
        travel_map[src].sort()
        used[src] = [False] * len(travel_map[src])  # 해당 출발지에서 사용된 티켓 관리

    answer = []
    get_route(travel_map, "ICN", answer, used, len(tickets)+1)

    return answer

def get_route(travel_map, src, route, used, total_len):
        route.append(src)

        # 모든 티켓을 사용했으면 경로 반환
        if len(route) == total_len:
            return True

        if src not in travel_map:
            route.pop()
            return False

        for i, dest in enumerate(travel_map[src]):
            if not used[src][i]:  # 사용되지 않은 티켓만 탐색
                used[src][i] = True
                if get_route(travel_map, dest, route, used, total_len):  # 경로가 완성되면 즉시 반환
                    return True
                used[src][i] = False  # 백트래킹
        
        route.pop()  # 되돌리기
        return False

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))