'''

https://school.programmers.co.kr/learn/courses/30/lessons/77486
- Programmers 77486 다단계 칫솔 판매 (Lv.3)
- DFS

'''

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]

    enroll_dic = defaultdict(int)
    for idx, val in enumerate(enroll):
        enroll_dic[val] = idx


    for i in range(len(seller)):
        idx = enroll_dic[seller[i]]
        profit = amount[i] * 100

        answer[idx] += profit - (profit // 10)
        profit //= 10 

        while referral[idx] != '-' and profit > 0 :
            idx = enroll_dic[referral[idx]]
            answer[idx] += profit - (profit // 10)
            profit //= 10

    return answer
