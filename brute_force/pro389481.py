'''

https://school.programmers.co.kr/learn/courses/30/lessons/389481
- Programmers 389481 봉인된 주문 (Lv.3)
- Brute Force

'''

def solution(n, bans):

    # bans 정렬: 길이순, 사전순
    bans = sorted(bans, key = lambda x : (len(x), x))
    
    # 길이 별 bans 분류
    bans_len = [[] for _ in range(12)]
    for i in bans:
        bans_len[len(i)].append(i)

    # 1~11 문자열 길이 경우의 수 
    cases = [0]
    for i in range(1, 12):
        cases.append(26**i)
    
    # n 번째의 문자열 길이
    length = 0
    for i in range(len(cases)):
        if cases[i] >= n:
            length = i
            break 
    
    # 찾아야 하는 문자열 = (n) + (n보다 앞 순서인 ban 당한 문자열 개수) 번째 문자열
    for i in range(length):
        n += len(bans_len[i])

    for word in bans_len[length]:
        temp = list(word)
        idx = 0
        place = len(temp) - 1
        for t in temp:
            idx += (ord(t)-ord('a')+1) * (26**place)
            place -= 1

        if idx <= n:
            n += 1
        else:
            break
    
    # n 번째 문자열 찾기
    answer = ''
    while n:
        n -= 1
        remain = n % 26
        answer = chr(ord('a')+remain) + answer 
        n //= 26  

    return answer
