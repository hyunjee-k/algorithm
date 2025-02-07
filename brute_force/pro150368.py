'''

https://school.programmers.co.kr/learn/courses/30/lessons/150368
- Programmers 150368 이모티콘 할인행사 (Lv.2)
- Brute Force

'''

from itertools import product

def solution(users, emoticons):
    answer = [0, 0]

    for emoticon_dc in product([10, 20, 30, 40], repeat=len(emoticons)):
        total_sales = 0
        total_signup = 0
        for u in users:
            amount = 0
            for idx, dc in enumerate(emoticon_dc):
                if u[0] > dc: continue
                amount += int((100 - dc) * 0.01 * emoticons[idx])
            
            if u[1] <= amount: total_signup += 1
            else: total_sales += amount
        
        if (total_signup > answer[0]) or (total_signup == answer[0] and total_sales > answer[1]):
            answer[0] = total_signup
            answer[1] = total_sales

    return answer
