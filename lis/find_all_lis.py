'''
모든 증가하는 최장 부분 수열을 찾는 방법
시간 복잡도: O(N^2)

'''

import sys
from bisect import bisect_left
from collections import defaultdict

class AllLIS:
    def __init__(self): 
        self.arr = list(map(int, sys.stdin.readline().split()))  # 수열
        self.n = len(self.arr) # 수열의 크기기

    def find_all_lis(self):
        sub_seq = []  # LIS의 길이를 계산하는 배열
        all_lis = defaultdict(list)  # 각 길이에 대한 모든 LIS를 저장

        for i in range(self.n):
            pos = bisect_left(sub_seq, self.arr[i])
            if pos == len(sub_seq):
                sub_seq.append(self.arr[i])
            else:
                sub_seq[pos] = self.arr[i]

            # 현재 길이(pos + 1)에 대해 경로 갱신
            if pos == 0:
                all_lis[pos + 1].append([self.arr[i]])  # 길이가 1인 경우
            else:
                for path in all_lis[pos]:
                    all_lis[pos + 1].append(path + [self.arr[i]])

        lis_length = len(sub_seq)
        unique_lis = self.remove_duplication(all_lis[lis_length])
        return lis_length, unique_lis
    
    def remove_duplication(self, all_sequence):
        unique_lis = []
        seen = set()
        for seq in all_sequence:
            seq_tuple = tuple(seq)  # 리스트를 튜플로 변환 (해시 가능)
            if seq_tuple not in seen:
                seen.add(seq_tuple)
                unique_lis.append(seq)  # 중복이 아닌 경우 추가

        return unique_lis

if __name__ == "__main__":
    lis_solver = AllLIS()
    lis_length, lis_sequences = lis_solver.find_all_lis()
    
    # LIS 길이 출력
    print(lis_length)
    
    # 모든 LIS 출력
    for seq in lis_sequences:
        print(*seq)

'''
- input
1 3 2 2 5 4

- output
3
1 3 5
1 2 5
1 3 4
1 2 4
'''

'''
- input
-60 -41 -100 8 -8 -52 -62 -61 -76 -52 -52 14 -11 -2 -54 46

- output
7
-60 -41 8 -52 14 -2 46
-60 -41 -8 -52 14 -2 46
-60 -41 -61 -52 14 -2 46
-60 -52 -61 -52 14 -2 46
-100 -52 -61 -52 14 -2 46
-60 -62 -61 -52 14 -2 46
-100 -62 -61 -52 14 -2 46
-60 -41 8 -52 -11 -2 46
-60 -41 -8 -52 -11 -2 46
-60 -41 -61 -52 -11 -2 46
-60 -52 -61 -52 -11 -2 46
-100 -52 -61 -52 -11 -2 46
-60 -62 -61 -52 -11 -2 46
-100 -62 -61 -52 -11 -2 46
'''