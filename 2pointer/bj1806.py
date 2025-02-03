'''

https://www.acmicpc.net/problem/1806
- 백준 1806 부분합 (골드4)
- 2 pointer

'''

import sys 

class TwoPointer:
    def __init__(self):
        ###########
        # TC 입력 #
        ###########

        # 수열의 길이 n, 목표하는 합 s
        self.n, self.s = map(int, sys.stdin.readline().split())
        # 수열 numbers
        self.numbers = list(map(int, sys.stdin.readline().split()))

    def calc(self):
        left = 0
        right = 0
        total = self.numbers[0]
        shortest = float('inf')
        
        while left <= right:
            if self.s <= total:
                shortest = min(shortest, right - left + 1)
                if shortest == 1: # 1보다 짧을 수 없으므로 탐색 종료
                    return 1
                total -= self.numbers[left]
                left += 1
            else:
                right += 1
                if right >= self.n: break
                total += self.numbers[right]

        if shortest == float('inf'):
            return 0

        return shortest
    


if __name__ == "__main__": 
    tp = TwoPointer()
    print(tp.calc())