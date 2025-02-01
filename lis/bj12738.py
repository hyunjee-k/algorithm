'''

https://www.acmicpc.net/problem/12738
- 백준 12738 가장 긴 증가하는 부분 수열 3 (골드2)
- binary search

LIS (Longest Increasing Subsequence)

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
        sub_seq = []
        for i in self.arr:
            pos = bisect_left(sub_seq, i)
            if pos == len(sub_seq):
                sub_seq.append(i)
            else:
                sub_seq[pos] = i
        
        return sub_seq
    


if __name__ == "__main__":
    lis = LIS()

    print(len(lis.find_lis()))

