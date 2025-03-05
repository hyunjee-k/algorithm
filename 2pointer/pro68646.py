'''

https://school.programmers.co.kr/learn/courses/30/lessons/68646
- Programmers 68646 풍선 터트리기 (Lv.3)
- 2 pointer

'''

def solution(a):
    n = len(a)
    if n <= 2:
        return n  # 풍선이 2개 이하면 모두 남을 수 있음
    
    answer = 2  # 양 끝 풍선은 무조건 남을 수 있음
    left_min = a[0]  # 왼쪽에서 최소값 갱신용
    right_min = [0] * n  # 오른쪽 최소값을 저장할 배열
    
    # 오른쪽 최소값 배열을 미리 계산
    right_min[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(a[i], right_min[i + 1])
    
    # 중앙 풍선들 검사
    for i in range(1, n - 1):
        if a[i] > left_min and a[i] > right_min[i + 1]:
            continue  # 양옆보다 크면 남을 수 없음
        
        answer += 1
        left_min = min(left_min, a[i])  # 왼쪽 최소값 갱신
    
    return answer
