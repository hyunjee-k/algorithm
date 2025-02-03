'''

https://www.acmicpc.net/problem/1644
- 백준 1644 소수의 연속합 (골드3)
- 2 pointer

수학 - 소수, 에라토스테네스의 체

'''

import sys
import math

n = int(sys.stdin.readline())

# 에라토스테네스의 체
def eratos(number):
    if number < 2:
        return []
    arr = [True for _ in range(number + 1)]
    arr[0], arr[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(number)) + 1): 
        if arr[i]:
            for j in range(i * i, number + 1, i):
                arr[j] = False

    return [i for i in range(2, number + 1) if arr[i]]  # 소수 리스트 반환

# 투 포인터 알고리즘
def two_pointer(target, prime_number):
    left, right, count = 0, 0, 0
    total = prime_number[0] if prime_number else 0  # 빈 리스트 처리
    
    while left <= right and right < len(prime_number):
        if total < target:
            right += 1
            if right == len(prime_number):
                break  # OutOfIndex 방지
            total += prime_number[right]
        elif total > target:
            total -= prime_number[left]
            left += 1
        else:
            count += 1
            total -= prime_number[left]
            left += 1

    return count

# 결과 출력 
prime_number = eratos(n)
answer = two_pointer(n, prime_number)

print(answer)
