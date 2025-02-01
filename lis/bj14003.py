'''

https://www.acmicpc.net/problem/14003
- 백준 14003 가장 긴 증가하는 부분 수열 5 (플레티넘5)
- binary search

LIS (Longest Increasing Subsequence)
수열 구하기

'''

import sys
from bisect import bisect_left

class LIS:
    def __init__(self): 
        ###########
        # TC 입력 #
        ###########

        # 첫째줄: 수열의 크기 n
        self.n = int(sys.stdin.readline())

        # 둘째줄: 수열
        self.arr = list(map(int, sys.stdin.readline().split()))

    def find_lis(self):
        sub_seq = []  # LIS의 길이를 계산하는 배열
        positions = []   # sub_seq에서 각 위치의 실제 arr 인덱스
        parent = [-1] * self.n  # LIS를 추적하기 위한 배열

        for i in range(self.n):
            pos = bisect_left(sub_seq, self.arr[i])
            if pos == len(sub_seq):
                sub_seq.append(self.arr[i])
                positions.append(i)
            else:
                sub_seq[pos] = self.arr[i]
                positions[pos] = i
            
            if pos > 0:
                parent[i] = positions[pos - 1]  # 이전 원소 인덱스 추적

        # LIS 재구성
        lis_length = len(sub_seq)
        lis = []
        current = positions[-1]  # LIS의 마지막 원소의 인덱스
        while current != -1:
            lis.append(self.arr[current])
            current = parent[current]
        lis.reverse()

        return lis_length, lis

if __name__ == "__main__":
    lis = LIS()
    lis_length, lis_sequence = lis.find_lis()
    print(lis_length)
    print(*lis_sequence)
    
