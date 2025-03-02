'''

https://school.programmers.co.kr/learn/courses/30/lessons/181188
- Programmers 181188 요격 시스템 (Lv.2)
- Greedy

'''

def solution(targets):
    targets = sorted(targets, key = lambda x:x[1])
    
    intercept = 0
    answer = 0
    for t in targets:
        if intercept > t[0]: continue
        intercept = t[1]
        answer += 1
    
    return answer


res = solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
print(res)