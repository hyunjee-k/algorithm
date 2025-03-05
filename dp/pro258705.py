'''

https://school.programmers.co.kr/learn/courses/30/lessons/258705
- Programmers 258705 산 모양 타일링 (Lv.3)
- DP

'''

def solution(n, tops):
    # 우측 하단을 공유하는 경우
    share = [0] * n
    # 우측 하단을 공유하지 않는 경우
    not_share = [0] * n

    if tops[0] == 1:
        share[0] = 4
        not_share[0] = 3
    else:
        share[0] = 3
        not_share[0] = 2
    
    for i in range(1, n):
        if tops[i] == 1:
            share[i] = (share[i-1] * 3 + not_share[i-1]) % 10007
            not_share[i] = (share[i-1] * 2 + not_share[i-1]) % 10007
        else:
            share[i] = (share[i-1] * 2 + not_share[i-1]) % 10007
            not_share[i] = (share[i-1] * 1 + not_share[i-1]) % 10007

    return share[-1]
