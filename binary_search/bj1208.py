'''

https://www.acmicpc.net/problem/1208
- 백준 1208 부분수열의 합2 (골드1)
- binary search

- 중간에서 만나기

'''

import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 부분 수열의 합 구하기
def get_subsequence_sum(sequence):
    subsequence_sum = []
    for i in range(len(sequence) + 1):
        for comb in combinations(sequence, i): # 조합 이용
            subsequence_sum.append(sum(comb))
    
    return subsequence_sum

# 배열을 반으로 나누기
left_arr = arr[:n//2]
right_arr = arr[n//2:]

# 각 부분에서 부분수열의 합 구하기
left_sum = get_subsequence_sum(left_arr)
right_sum = get_subsequence_sum(right_arr)

# 합이 S가 되는 개수 찾기
count = 0
right_sum.sort() # 이진 탐색을 위해 정렬 
for left in left_sum:
    target = s - left
    count += bisect_right(right_sum, target) - bisect_left(right_sum, target)

# 공집합(둘 다 비었을 때)이 고려되는 경우, 0을 세지 않도록 처리
if s == 0:
    count -= 1

# 정답 출력 
print(count)