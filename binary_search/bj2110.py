'''

https://www.acmicpc.net/problem/2110
- 백준 2110 공유기 설치 (골드4)
- binary search

d = 두 공유기 사이의 거리 
결정문제로 변환: 최소 d 로 c 개의 공유기 설치 가능한지 판단

'''

import sys

class BinarySearch:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 첫째줄: 집의 개수 n, 공유기의 개수 c
        self.n, self.c = map(int, sys.stdin.readline().split())

        # 집의 좌표
        self.house = [int(sys.stdin.readline()) for _ in range(self.n)]

    def can_set_routers(self, distance):
        # 첫번째 집에 공유기 설치
        count = 1
        last_position = self.house[0]

        # 현재 집과 마지막 설치 위치의 거리가 기준 거리 이상인지 확인
        for i in range(1, self.n):
            if self.house[i] - last_position >= distance:
                count += 1
                last_position = self.house[i]
                if count >= self.c: 
                    return True
                
        return False

    def binary_search(self, left, right):
        result = 0

        while left <= right:
            mid = (left + right) // 2

            if self.can_set_routers(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result



if __name__ == "__main__":
    bs = BinarySearch()

    # 집의 좌표 정렬
    bs.house.sort()

    # 이분 탐색으로 가장 인접한 두 공유기의 최대 거리 찾기
    answer = bs.binary_search(1, bs.house[bs.n - 1] - bs.house[0])
    print(answer)
