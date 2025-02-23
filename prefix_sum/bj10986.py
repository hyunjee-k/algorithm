'''

https://www.acmicpc.net/problem/10986
- 백준 10986 나머지 합 (골드3)
- 구간 합 

'''

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = [0]*m # c[i] = 나머지가 i 인 경우의 수
prefix_sum = 0 
answer = 0

# 시간 복잡도: O(N)
for i in range(n):
    prefix_sum += arr[i]
    remainder = prefix_sum % m

    # 나머지가 0인 경우는 추후 계산 시 제대로 집계되지 않으므로 미리 합산
    if remainder == 0:
        answer += 1

    cnt[remainder] += 1

# 조합: kC2 = k(k-1)/2
# cnt[i] = k: 나머지가 i 인 것이 k개 있고, 
#             그 중 2개를 뽑는 경우의 수를 세면 모든 구간의 조합을 구할 수 있다
for k in cnt:
    answer += (k*(k-1)) // 2

print(answer)