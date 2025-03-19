'''

https://www.acmicpc.net/problem/2473
- 백준 2473 세 용액 (골드3)
- 2 pointer

'''

import sys

# 용액의 개수 n
n = int(sys.stdin.readline())
# 용액 arr
arr = list(map(int, sys.stdin.readline().split()))

def solution():
    # 용액 정보를 오름차순 정렬
    arr.sort()

    answer = []
    min_abs = float('inf')
    for i in range(n-2):
        l = i + 1
        r = n - 1
        while l < r:
            tmp = arr[i] + arr[l] + arr[r]
            if tmp == 0:
               return [arr[i], arr[l], arr[r]]

            if abs(tmp) < min_abs:
                min_abs = abs(tmp)
                answer = [arr[i], arr[l], arr[r]]

            if tmp < 0:
                l += 1
            else:
                r -= 1

    return answer    

print(*solution())
