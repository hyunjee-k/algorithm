'''

https://www.acmicpc.net/problem/2352
- 백준 2352 반도체 설계 (골드2)
- binary search

LIS (Longest Increasing Subsequence)

'''

import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
port_numbers = list(map(int, sys.stdin.readline().split()))

def find():
    connection = []
    for port in port_numbers:
        idx = bisect_left(connection, port)
        if idx == len(connection):
            connection.append(port)
        else:
            connection[idx] = port
    
    return len(connection)


print(find())