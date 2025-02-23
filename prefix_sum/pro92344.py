'''

https://school.programmers.co.kr/learn/courses/30/lessons/92344
- Programmers 92344 파괴되지 않은 건물 (Lv.3)
- 누적합

'''

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    durability = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # type=1 공격, type=2 회복
            degree *= -1
        
        durability[r1][c1] += degree
        durability[r1][c2+1] -= degree
        durability[r2+1][c1] -= degree
        durability[r2+1][c2+1] += degree
    
    for i in range(n):
        for j in range(m):
            if j+1 < m:
                durability[i][j+1] += durability[i][j]

    for i in range(n):
        for j in range(m):
            durability[i+1][j] += durability[i][j]

    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += durability[i][j]
            if board[i][j] > 0: answer += 1

    return answer




board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
answer = solution(board, skill)
print(answer)
