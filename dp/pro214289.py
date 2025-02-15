'''

https://school.programmers.co.kr/learn/courses/30/lessons/214289
- Programmers 214289 에어컨 (Lv.3)
- dp

'''


def solution(temperature, t1, t2, a, b, onboard):
    # 생각하기 편하게 실외온도는 무조건 희망온도보다 높도록 설정
    if temperature < t1:
        temperature = t2 + (t1 - temperature)

    # temperature 와 희망 온도의 온도 차이
    diff = temperature - t2

    # temperature에서 희망온도까지 소비전력
    diff_w = diff * a

    # 희망온도에서 온도 유지 시 소비전력
    # 간격1: 1 조절(a) or 유지(b)
    step1_w = min(a, b)
    # 간격2: 1 조절과 끄기(a+0) || 유지 2번(b*2)
    step2_w = min(a, b * 2)


    # temperature 에서 시작하는 최초 탑승 간격 = temperature 에서 희망온도까지 소비전력/step2 소비전력의 반
    temperature_step = diff_w / (step2_w / 2)

    # 탑승 인덱스
    board_index = [i for i, v in enumerate(onboard) if v]

    # 탑승 간격
    board_interval = []
    for i in range(len(board_index) - 1):
        board_interval.append(board_index[i + 1] - board_index[i])

    # temperature_step 찾기
    step = [0 if i > temperature_step else i for i in board_interval]

    # temperature_step 기준으로 간격 합
    l = []
    while True:
        try:
            l.append(sum(step[: step.index(0)]))
            step = step[step.index(0) + 1 :]
        except:
            l.append(sum(step))
            break

    # temperature_step 총 소비전력
    total_diff_w = len(l) * diff_w

    # 나머지 총 소비전력
    remain_step_w = sum([sum(((i // 2) * step2_w, (i % 2) * step1_w)) for i in l])

    return total_diff_w + remain_step_w