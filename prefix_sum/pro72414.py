'''

https://school.programmers.co.kr/learn/courses/30/lessons/72414
- Programmers 72414 광고 삽입 (Lv.3)
- 누적합

'''


def solution(play_time, adv_time, logs):

    play_sec = convert_to_sec(play_time)
    adv_sec = convert_to_sec(adv_time)

    views = [0 for _ in range(play_sec+1)]
    for l in logs:
        tmp = l.split('-')
        start = convert_to_sec(tmp[0])
        end = convert_to_sec(tmp[1])
        # 시청 시작 지점에 +1, 시청 종료 지점에 -1
        views[start] += 1
        views[end] -= 1

    # 초 별 시청자 수 
    for i in range(1, play_sec+1):
        views[i] += views[i-1]
    
    # 초 별 누적 시청자 수 
    for i in range(1, play_sec+1):
        views[i] += views[i-1]

    # 최다 시청 구간 찾기
    max_view = views[adv_sec - 1]  # 처음 구간 (0초 ~ adv_sec)
    max_start = 0

    for i in range(1, play_sec - adv_sec + 1):  # 가능한 모든 구간 확인
        curr_view = views[i + adv_sec - 1] - views[i - 1]
        if curr_view > max_view:
            max_view = curr_view
            max_start = i

    return convert_to_time(max_start)
        

def convert_to_sec(time):
    tmp = time.split(':')
    sec = int(tmp[0]) * 3600 + int(tmp[1]) * 60 + int(tmp[2])

    return sec

def convert_to_time(sec):
    hh = str(sec // 3600)
    if len(hh) == 1:
        hh = '0' + hh 
    
    sec %= 3600
    mm = str(sec // 60)
    if len(mm) == 1:
        mm = '0' + mm
    
    sec %= 60
    ss = str(sec)
    if len(ss) == 1:
        ss = '0' + ss

    return hh + ":" + mm + ":" + ss
