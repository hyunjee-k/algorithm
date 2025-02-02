'''

https://school.programmers.co.kr/learn/courses/30/lessons/132265
- Programmers 132265 롤케이크 자르기 (Lv.2)
- Sliding Window

주석이 내가 푼 풀이

'''

from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer


'''
from collections import defaultdict 

def solution(topping):
    answer = 0
    a = cut_a(topping)
    b = cut_b(topping)
    for i in range(len(topping)-1):
        if a[i] == b[i+1]:
            answer += 1
    return answer

def cut_a(topping):
    a_topping = defaultdict(int)
    a_topping[topping[0]] = 1
    a_count = [0 for _ in range(len(topping))]
    a_count[0] = 1
    
    for i in range(1, len(topping)):
        if a_topping[topping[i]] == 0:
            a_topping[topping[i]] = 1
            a_count[i] = a_count[i-1] + 1
        else:
            a_count[i] = a_count[i-1]
    
    return a_count

def cut_b(topping):
    b_topping = defaultdict(int)
    b_topping[topping[-1]] = 1
    b_count = [0 for _ in range(len(topping))]
    b_count[-1] = 1
    
    for i in range(len(topping)-2, -1, -1):
        if b_topping[topping[i]] == 0:
            b_topping[topping[i]] = 1
            b_count[i] = b_count[i+1] + 1
        else:
            b_count[i] = b_count[i+1]
        
    return b_count

'''