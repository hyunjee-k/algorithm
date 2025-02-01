'''

https://www.acmicpc.net/problem/2512
- 백준 2512 예산 (실버2)
- binary search

target = 상한액
결정문제로 변환: target 기준으로 배당했을 때 m(총 예산)을 넘지 않는지 확인

'''

import sys

class BinarySearch:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 첫째줄: 지방의 수 n
        self.n = int(sys.stdin.readline())

        # 둘째줄: 각 지방의 요청 예산
        self.budget = list(map(int, sys.stdin.readline().split()))

        # 셋째줄: 총 예산 m
        self.m = int(sys.stdin.readline())

    def is_avaliable_budget(self, target):
        total = 0
        for b in self.budget:
            if b <= target:
                total += b
            else:
                total += target
        
        if total > self.m:
            return False
        
        return True
    
    def binary_search(self, left, right):
        limit = 0
        while left <= right:
            mid = (left + right) // 2

            if self.is_avaliable_budget(mid):
                left = mid + 1
                limit = mid
            else:
                right = mid - 1

        return limit
    


if __name__ == "__main__":
    bs = BinarySearch()

    bs.budget.sort()

    answer = bs.binary_search(0, bs.budget[-1])
    if answer > sum(bs.budget):
        answer = bs.budget[-1]

    print(answer)
