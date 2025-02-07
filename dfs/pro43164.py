'''

https://school.programmers.co.kr/learn/courses/30/lessons/43164
- Programmers 43164 여행경로 (Lv.3)
- DFS

'''

from collections import defaultdict 

def dfs(graph, N, key, footprint):

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets)

    for src, dest in tickets:
        graph[src].append(dest)
        graph[src].sort()

    # ICN 부터 시작
    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer