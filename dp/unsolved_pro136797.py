'''

https://school.programmers.co.kr/learn/courses/30/lessons/136797
- Programmers 136797 숫자 타자 대회 (Lv.3)
- DP

[!!!미완성!!!]

'''

from collections import defaultdict

def solution(numbers):
    numbers = list(numbers)
    keypad = init_keypad()
    weight = init_weight(keypad)

    # dp[i][l][r] = i번째 숫자를 누를 때 왼손은 l, 오른손은 r에 있을 때 최소 비용
    dp = defaultdict(lambda: float('inf'))
    dp[(0,4,6)] = 0

    for i, num in enumerate(numbers):
        next_dp = defaultdict(lambda: float('inf'))
        target = key_to_idx(num)
        for (_, left, right), cost in dp.items():
            
            if left == target:
                next_dp[(i+1, target, right)] = cost + 1
                continue
            if right == target:
                next_dp[(i+1, left, target)] = cost + 1
                continue

            # 왼손으로 누르는 경우
            new_cost = cost + weight[left][target]
            next_dp[(i + 1, target, right)] = min(next_dp[(i+1, target, right)], new_cost)

            # 오른손으로 누르는 경우
            new_cost = cost + weight[right][target]
            next_dp[(i + 1, left, target)] = min(next_dp[(i+1, left, target)], new_cost)

        dp = next_dp  # DP 테이블 업데이트

    # 최소 비용 반환
    return min(dp.values())


def calc_weight(src, dest):
    if src == dest: return 1
    
    x = abs(src[0]-dest[0])
    y = abs(src[1]-dest[1])
    weight = 0
    while x != 0 or y != 0:
        if x > 0 and y > 0:
            weight += 3
            x -= 1
            y -= 1
            continue
        if x > 0:
            weight += 2
            x -= 1
        elif y > 0:
            weight += 2
            y -= 1

    return weight


def init_weight(keypad):
    weight = [[0 for _ in range(13)] for _ in range(13)]
    for i in range(1, 13):
        for j in range(i, 13):
            w = calc_weight(keypad[idx_to_key(i)], keypad[idx_to_key(j)])
            weight[i][j] = w
            weight[j][i] = w

    return weight


def init_keypad():
    keypad = dict()
    for i in range(4):
        for j in range(3):
            keypad[idx_to_key(i*3+j+1)] = (i,j)
    
    return keypad


def idx_to_key(idx):
    if idx == 10: 
        return '*'
    elif idx == 11: 
        return '0'
    elif idx == 12:
        return '#'
    else: 
        return str(idx)
    

def key_to_idx(key):
    if key == '*': 
        return 10
    elif key == '0': 
        return 11
    elif key == '#':
        return 12
    else: 
        return int(key)




answer = solution("25125") #32221
print(answer)