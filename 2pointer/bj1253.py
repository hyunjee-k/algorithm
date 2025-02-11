'''

https://www.acmicpc.net/problem/1253
- 백준 1253 좋다 (골드4)
- 2 pointer

'''

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

def two_pointer():
    good = 0

    for i in range(n):
        left = 0
        right = n-1
        
        while left < right:
            if left == i:
                left += 1
                continue
            elif right == i:
                right -= 1
                continue
            
            if arr[left] + arr[right] == arr[i]:
                good += 1
                break

            if arr[left] + arr[right] > arr[i]:
                right -= 1
            else:
                left += 1

    return good 


print(two_pointer())