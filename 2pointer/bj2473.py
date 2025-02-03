'''

https://www.acmicpc.net/problem/2473
- 백준 2473 세 용액 (골드3)
- 2 pointer

'''

import sys

class TwoPointer:
    def __init__(self):
        # 용액의 개수 n
        self.n = int(sys.stdin.readline())
        # 용액 arr
        self.arr = list(map(int, sys.stdin.readline().split()))
        self.arr.sort()

    def solution(self):
        result = []
        min_abs = float('inf')

        for i in range(self.n-2):
            left = i + 1
            right = self.n - 1
            while left < right:
                total = self.arr[i] + self.arr[left] + self.arr[right]
                if abs(total) < min_abs:
                    min_abs = abs(total)
                    result = [self.arr[i], self.arr[left], self.arr[right]]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else: # 합이 0이면 바로 종료 가능
                    return result 

        return result
    

if __name__ == "__main__":
    tp = TwoPointer()
    answer = tp.solution()
    
    print(*answer)