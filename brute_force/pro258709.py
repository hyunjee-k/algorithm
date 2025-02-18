'''

https://school.programmers.co.kr/learn/courses/30/lessons/258709
- Programmers 258709 주사위 고르기 (Lv.3)
- Brute Force

'''

from itertools import combinations
from collections import defaultdict

def solution(dice):
    size = len(dice)

    # 주사위 조합별 가능한 합 계산
    combinations_list = list(combinations(range(size), size // 2))
    sum_dict = {c: get_sum(dice, c, 0, 0, defaultdict(int)) for c in combinations_list}

    max_win_count = 0
    winning_combination = []

    # A와 B 간의 승리 횟수 계산
    for i in range(len(combinations_list) // 2):
        a = combinations_list[i]
        b = combinations_list[-i - 1]

        a_sum = sorted([key for key in sum_dict[a]])
        b_sum = sorted([key for key in sum_dict[b]])

        # A의 승리 수 계산
        a_win = 0
        for k in a_sum:
            b_cursor = 0
            while b_cursor < len(b_sum) and b_sum[b_cursor] < k:
                a_win += (sum_dict[a][k] * sum_dict[b][b_sum[b_cursor]])
                b_cursor += 1

        # B의 승리 수 계산
        b_win = 0
        for k in b_sum:
            a_cursor = 0
            while a_cursor < len(a_sum) and a_sum[a_cursor] < k:
                b_win += (sum_dict[b][k] * sum_dict[a][a_sum[a_cursor]])
                a_cursor += 1

        # 승리 수 중 더 큰 쪽을 기준으로 최적의 팀 선택
        if a_win > max_win_count:
            max_win_count = a_win
            winning_combination = a

        if b_win > max_win_count:
            max_win_count = b_win
            winning_combination = b

    return [x + 1 for x in winning_combination]

# 주사위 조합 별 가질 수 있는 눈의 합  구하기
def get_sum(dice, combi, idx, total, sum_list): 
    if idx == len(combi):
        sum_list[total] += 1
        return sum_list
    
    for i in dice[combi[idx]]:
        get_sum(dice, combi, idx+1, total+i, sum_list)

    return sum_list
