'''

https://school.programmers.co.kr/learn/courses/30/lessons/92343
- Programmers 92343 양과 늑대 (Lv.3)
- DFS

- 설명: https://blog.encrypted.gg/1029

'''

left = [-1] * 20 # 왼쪽 자식
right = [-1] * 20 # 오른쪽 자식
val = [] # 양/늑대 값
n = 0
answer = 1
visit = [0] * (1 << 17) # visit[x] : 상태 x 방문 여부

def solution(info, edges):
    global n, val
    n = len(info)
    val = info[:]

    for src, dest in edges:
        if left[src] == -1: left[src] = dest
        else: right[src] = dest

    dfs(1)
    return answer

def dfs(state):
    global answer

    if visit[state]: return None

    visit[state] = 1
    wolf = 0 # 늑대 수
    total_node = 0 # 전체 정점의 수  
    for i in range(n):
        if state & (1 << i):
            total_node += 1
            wolf += val[i]
        
    # 늑대가 1/2 이상인 경우 종료
    if wolf*2 >= total_node: return None 

    # 현재 양의 수가 answer보다 큰 경우 갱신 
    answer = max(answer, total_node-wolf)

    # 자식 노드 탐색
    for i in range(n):
        # 선택된 노드가 아닌 경우 건너뜀 
        if not state & (1<<i): continue 

        if left[i] != -1:
            dfs(state | (1<<left[i]))
        if right[i] != -1:
            dfs(state | (1<<right[i]))
