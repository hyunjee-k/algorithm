'''

https://school.programmers.co.kr/learn/courses/30/lessons/155651
- Programmers 155651 호텔 대실 (Lv.2)
- 정렬과 스위핑

누적합으로 푼 풀이 참고하기

'''

import heapq

def solution(book_time):
    answer = 0
    book_time = convert_to_minute(book_time)
    heapq.heapify(book_time)
    answer = calc_room(book_time)
    
    return answer

def calc_room(book_time):
    total_room = 0
    using = []
    while book_time:
        start, end = heapq.heappop(book_time)
        while using:
            using_end = heapq.heappop(using)
            if using_end + 10 > start:
                heapq.heappush(using, using_end)
                break
        heapq.heappush(using, end)
        total_room = max(total_room, len(using))
        
    return total_room
        
def convert_to_minute(book_time):
    reservation = []
    for i in book_time:
        start = i[0].split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = i[1].split(':')
        end = int(end[0]) * 60 + int(end[1])
        reservation.append([start, end])
    
    return reservation

'''
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)
'''