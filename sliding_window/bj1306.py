'''

https://www.acmicpc.net/problem/1306
- 백준 1306 달려라 홍준 (플레티넘5)
- Sliding Window

'''

from collections import deque
import sys


# 입력 받기
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = []
sight = deque()  # 덱을 사용하여 최댓값을 유지

# 슬라이딩 윈도우 초기 설정
for i in range(min(2 * M - 1, N)):
    while sight and sight[-1][1] < arr[i]:
        sight.pop()
    sight.append((i, arr[i]))

# 첫 번째 윈도우에서의 최댓값
result.append(sight[0][1])

# 예외 처리: 윈도우가 완성되지 않은 경우
if min(2 * M - 1, N) != 2 * M - 1:
    print(*result)
    exit(0)

# 슬라이딩 윈도우 계산
for i in range(M, N - M + 1):
    # 윈도우 범위에서 벗어난 인덱스를 덱에서 제거
    if sight[0][0] <= i - M:
        sight.popleft()
    
    # 새로운 값을 덱에 추가
    while sight and sight[-1][1] < arr[i + M - 1]:
        sight.pop()
    
    sight.append((i + M - 1, arr[i + M - 1]))
    
    # 현재 윈도우에서의 최댓값
    result.append(sight[0][1])

# 결과 출력
print(*result)
