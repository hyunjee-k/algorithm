'''

https://school.programmers.co.kr/learn/courses/30/lessons/150366
- Programmers 150366 표 병합 (Lv.3)
- Union-Find

'''

excel = [['' for _ in range(51)] for _ in range(51)]
parent = [i for i in range(51*51)]


def solution(commands):
    global excel, parent
    answer = []
    
    for i in commands:
        tmp = i.split()
        command = tmp[0]
        values = tmp[1:]

        if command == 'UPDATE':
            if len(values) == 3:
                update(int(values[0]), int(values[1]), values[2])
            elif len(values) == 2:
                convertA2B(values[0], values[1])

        elif command == 'MERGE':
            merge(int(values[0]), int(values[1]),int(values[2]), int(values[3]))

        elif command == 'UNMERGE':
            unmerge(int(values[0]), int(values[1]))

        elif command == 'PRINT':
            answer.append(pprint(int(values[0]), int(values[1])))
        

    return answer 


def update(r, c, value):
    global excel

    root = find((r*51) + c)
    excel[root//51][root%51] = value

    return

def convertA2B(a, b):
    global excel

    for r in range(1, 51):
        for c in range(1, 51):
            if excel[r][c] == a:
                excel[r][c] = b 
    
    return

def merge(r1, c1, r2, c2):
    global excel

    root_x = find((r1*51)+c1)
    root_y = find((r2*51)+c2)

    # 같은 셀이면 병합 명령 무시하기
    if root_x == root_y: return 

    # 병합
    union((r1*51)+c1, (r2*51)+c2)

    # 값 갱신 
    if excel[root_x//51][root_x%51] == '':
        excel[root_x//51][root_x%51] = excel[root_y//51][root_y%51]
        
    excel[root_y//51][root_y%51] = ''

    return

def unmerge(r, c):
    global excel, parent

    root = find((r*51) + c)

    # 병합 해제할 곳의 값 구하기
    value = excel[root//51][root%51]

    # 병합 해제 대상의 셀 구하기  
    same = []
    for i in range(1, 51):
        for j in range(1, 51):
            if find(i*51+j) == root:
                same.append(i*51+j)

    # 병합 해제 및 값 초기화
    while same:
        i = same.pop()
        parent[i] = i
        excel[i//51][i%51] = ''

    # 값 할당
    excel[r][c] = value
    return

def pprint(r, c):
    global excel

    root = find((r*51) + c)
    if excel[root//51][root%51] == '':
        return 'EMPTY'
    return excel[root//51][root%51]

def find(x):
    global parent 
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x, y):
    global parent

    root_a = find(x)
    root_y = find(y)
    if root_a != root_y:
        parent[root_y] = root_a

    return 

