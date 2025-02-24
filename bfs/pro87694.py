'''

https://school.programmers.co.kr/learn/courses/30/lessons/87694
- Programmers 87694 아이템 줍기 (Lv.3)
- BFS

'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j] *= 4
    
    characterX *= 4
    characterY *= 4
    itemX *= 4
    itemY *= 4


    dq = deque()
    visit = [[0 for _ in range(201)] for _ in range(201)]
    
    rects = find_rectangle(rectangle, -1, characterX, characterY)
    visit[characterY][characterX] = 1
    for r in rects:        
        dq.append((r, characterX, characterY, 0))

    while dq:
        r, x, y, distance = dq.popleft()

        if x == itemX and y == itemY:
            return distance//4

        x1, y1, x2, y2 = rectangle[r]
        if x1 == x or x2 == x:
            if y+1 <= y2 and visit[y+1][x] == 0 and can_visit(rectangle, x, y+1):
                rect = find_rectangle(rectangle, r, x, y+1)
                visit[y+1][x] = 1
                dq.append((rect, x, y+1, distance+1))

            if y-1 >= y1 and visit[y-1][x] == 0 and can_visit(rectangle, x, y-1):
                rect = find_rectangle(rectangle, r, x, y-1) 
                visit[y-1][x] = 1
                dq.append((rect, x, y-1, distance+1))
        
        if y1 == y or y2 == y:
            if x+1 <= x2 and visit[y][x+1] == 0 and can_visit(rectangle, x+1, y):
                rect = find_rectangle(rectangle, r, x+1, y)
                visit[y][x+1] = 1
                dq.append((rect, x+1, y, distance+1))
            
            if x-1 >= x1 and visit[y][x-1] == 0 and can_visit(rectangle, x-1, y):
                rect = find_rectangle(rectangle, r, x-1, y)
                visit[y][x-1] = 1
                dq.append((rect, x-1, y, distance+1))

    return 0


# x, y 가 있는 사각형을 찾는 함수
# rectangle: 사각형 정보
# cur: 기존에 있던 사각형의 인덱스
# 반환: 좌표를 포함한 사각형의 인덱스
def find_rectangle(rectangle, cur, x, y):
    rec = []
    for idx, (x1, y1, x2, y2) in enumerate(rectangle):
        if x == x1 or x == x2:
            if y1 <= y and y <= y2:
                rec.append(idx)
        elif y == y1 or y == y2:
            if x1 <= x and x <= x2:
                rec.append(idx)

    # 예외: 처음 시작이 두 사각형에 걸쳐있는 경우 
    if cur == -1:
        return rec
    
    # 사각형이 두개인 경우 cur과 다른 사각형을 반환하기 위함  
    for i in rec:
        if cur != i: return i

    return rec[0]

# x, y 를 방문할 수 있는지 판단하는 함수 
# 다른 사각형 안에 있으면 방문 불가 
def can_visit(rectangle, x, y):
    for x1, y1, x2, y2 in rectangle:
        if x1 < x and x < x2 and y1 < y and y < y2:
            return False
    
    return True




rectangle = [[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]]
res = solution(rectangle, 3,2,5,4)
print(res) # 8


