'''

https://www.acmicpc.net/problem/2632
- 백준 2632 피자판매 (골드2)
- binary search

'''

import sys
input_ = sys.stdin.readline

want = int(input_())
m, n = map(int, input_().split())
a = [int(input_()) for _ in range(m)]
b = [int(input_()) for _ in range(n)]


pizza = [0 for _ in range(want+1)]
for i in a:
    if i < want+1:
        pizza[i] += 1
for i in b:
    if i < want+1:
        pizza[i] += 1

print(pizza)