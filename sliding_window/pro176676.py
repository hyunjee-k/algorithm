'''

https://school.programmers.co.kr/learn/courses/30/lessons/17676
- Programmers 17676 추석 트래픽 (Lv.3)
- 누적합

'''

def solution(lines):

    times = []
    for line in lines:
        tmp = line.split()
        end_time = convert_milli(tmp[1]) 
        processing = convert_processing(tmp[2])
        start_time = end_time - processing + 1
        times.append((start_time // 1000, end_time // 1000))
    
    times = sorted(times, key = lambda k:k[0])
    
    min_time = times[0][0]
    max_time = times[-1][1]
    time_range = max_time - min_time + 1

    logs = [0 for _ in range(time_range)]
    for s, e in times:
        logs[s-min_time] += 1
        logs[e-min_time] -= 1

    for i in range(1, time_range):
        logs[i] += logs[i-1]

    print(logs)

    max_traffic = 0
    for i in logs:
        max_traffic = max(max_traffic, i)

    return max_traffic

def convert_milli(time):
    tmp = time.split(':')
    sec = tmp[2].split('.')
    milli = int(tmp[0]) * 3600000 + int(tmp[1]) * 60000 + int(sec[0]) * 1000 + int(sec[1])

    return milli

def convert_processing(procs):
    tmp = procs.split('.')
    if len(tmp) == 1:
        return int(tmp[0][:-1]) * 1000
    else:
        return int(tmp[0]) * 1000 + int(tmp[1][:-1])

lines =  [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
res = solution(lines)
print(res)