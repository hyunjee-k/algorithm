'''

https://school.programmers.co.kr/learn/courses/30/lessons/250135
- Programmers 250135 아날로그 시계 (Lv.2)
- Greedy

'''

def solution(h1, m1, s1, h2, m2, s2):

    '''
    [분침&초침]
    - 1분에 1번씩 만난다
    - 59분 -> 0분으로 갈 때는 만나지 않는다 

    [시침&초침]
    - 1분에 1번씩 만난다
    - 11시 -> 12시로 갈 때는 만나지 않는다
    '''

    # 00:00:00 ~ h1:m1:s1 
    cnt1 = count_from_midnight(h1, m1, s1)
    # 00:00:00 ~ h2:m2:s2
    cnt2 = count_from_midnight(h2, m2, s2)

    answer = cnt2 - cnt1
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0: answer += 1

    return answer

# 00:00:00 ~ h:m:s 까지 겹치는 횟수
def count_from_midnight(h, m, s):
    cnt = -1 

    # 시/분/초침 초당 이동 각도
    sec_deg = 360 / 60
    min_deg = 360 / (60*60)
    hour_deg = 360 / (60*60*12)

    # 종료 시점: h:m:s 일 때 시침/분침의 위치에 따라 만남 여부 계산
    total_sec = h * (60*60) + m * 60 + s
    s_deg = (total_sec * sec_deg) % 360
    m_deg = (total_sec * min_deg) % 360 
    h_deg = (total_sec * hour_deg) % 360

    if m_deg <= s_deg: cnt += 1
    if h_deg <= s_deg: cnt += 1

    # 초침이 시침/분침과 만나는 횟수 (=분당 각각 한번씩 만남)
    cnt += (h * 60 + m) * 2 # 종료시점의 분은 제외하고 카운팅

    # 분침 예외: 59분 -> 00분 (정각에서 만나므로 분침,초침이 안만남)
    cnt -= h

    # 시침 예외: 11시 -> 12시 (정오에서 만나므로 시침,초침이 안만남)
    if h >= 12:
        cnt -= 2
 
    return cnt

