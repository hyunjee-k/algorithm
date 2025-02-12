'''

https://www.acmicpc.net/problem/1300
- 백준 1300 k번째 수 (골드1)
- binary search

'''

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline()) 

'''
n=3, k=7

- n*n 배열은 다음과 같다
1 2 3
2 4 6
3 6 9

- 예를 들어 get_order(6)
1번 행: [1, 2, 3] -> 6//1 = 6, 행은 3이 최대이므로 min(6, 3) = 3
2번 행: [2, 4, 6] -> 6//2 = 3
3번 행: [3, 6, 9] -> 6//3 = 2

cnt = 3 + 3 + 2 = 8
배열에서 6 이하인 원소의 개수는 8개

'''

def get_order(number):
    # number 이하의 값이 몇 개 인지 반환하는 함수
    cnt = 0
    for i in range(1, n+1):
        cnt += min(number//i, n)

    return cnt

l = 1
r = k
while l <= r:
    mid = (l+r)//2
    if get_order(mid) >= k:
        r = mid - 1
    else:
        l = mid + 1


print(l)
