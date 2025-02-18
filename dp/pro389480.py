'''

https://school.programmers.co.kr/learn/courses/30/lessons/389480
- Programmers 389480 완전범죄 (Lv.2)
- dp

- 완전 탐색으로 풀 경우 2^40 -> dp나 greedy 고려
- greedy 로는 안풀리므로 dp 사용 

'''


def solution(info, n, m):
    size = len(info)

    # dp[x][y]
    # 물건 x개 훔쳤을 때: b 흔적 = y, a 흔적 = d[x][y]
    dp = [[float('inf') for _ in range(m)] for _ in range(size+1)]
    dp[0][0] = 0

    for i in range(1, size+1):
        a = info[i-1][0]
        b = info[i-1][1]

        for j in range(m):
            # a 가 훔칠 때
            dp[i][j] = min(dp[i][j], dp[i-1][j]+a)
            # b 가 훔칠 때
            if j + b < m:
                dp[i][j+b] = min(dp[i][j+b], dp[i-1][j])

    answer = min(dp[size])
    if answer < n: return answer
    
    return -1




info = [[3, 3], [3, 3]]
n = 6
m = 1

answer = solution(info, n, m)
print(answer)