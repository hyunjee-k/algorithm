'''

https://school.programmers.co.kr/learn/courses/30/lessons/131701
- Programmers 131701 연속 부분 수열의 합의 개수 (Lv.2)
- 누적합

'''

def solution(elements):
    answer = 0
    size = len(elements)
    
    # 중복 숫자 체크를 위한 배열
    number_check = [0 for _ in range(1000*1000 + 1)]
    # dp[i][j]: elements[j] 부터 시작하는 길이가 i 인 수열의 원소 합
    dp = [[0 for _ in range(size)] for _ in range(size+1)]
   
    # dp[1]: 길이가 1인 수열의 합 셋팅
    for i in range(size):
        dp[1][i] = elements[i]
        if number_check[elements[i]] == 0:
            number_check[elements[i]] = 1
            answer += 1

    # dp[2]~dp[size]: 길이가 2~size인 수열의 합 
    for i in range(2, size+1):
        for j in range(size):
            idx = j + i - 1
            if idx >= size:
                idx -= size
            dp[i][j] = dp[i-1][j] + elements[idx]

            # 숫자 중복 확인
            if number_check[dp[i][j]] == 0:
                answer += 1
                number_check[dp[i][j]] = 1

    return answer


def best_solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)