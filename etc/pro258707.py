'''

https://school.programmers.co.kr/learn/courses/30/lessons/258707
- Programmers 258707 n+1카드게임 (Lv.3)

- 그리디
- 이분 탐색
- 2 pointer

'''

def solution(coin, cards):
    n = len(cards)
    my_cards = cards[:n//3]
    answer = play_game(n, coin, cards, my_cards)
    return answer

def play_game(n, coin, cards, my_cards):
    keep_cards = []
    step = 0

    for i in range(n//3, n, 2):
        step += 1

        # 뽑은 두장은 보관
        keep_cards.append(cards[i])
        if i + 1 < n:
            keep_cards.append(cards[i+1])

        c1, c2 = make_target(n+1, my_cards)
        if c1 < 0 or c2 < 0: # 내 카드의 합이 n+1이 안되는 경우
            # coin 사용하여 keep_cards에서 카드 선택

            # coin 1개 사용
            if coin >= 1: 
                x1, x2 = make_target2(n+1, my_cards, keep_cards)
                if x1 >= 0 or x2 >= 0: # 가능한 경우 다음 턴 진행 
                    coin -= 1
                    del keep_cards[x2]
                    del my_cards[x1]
                    continue

            # coin 2개 사용 (coin 1개로 안되는 경우)
            if coin >= 2: 
                x1, x2 = make_target(n+1, keep_cards)
                if x1 < 0 or x2 < 0: # 게임 종료
                    return step
                else: # 가능한 경우 다음 턴 진행 
                    coin -= 2
                    del keep_cards[x2]
                    del keep_cards[x1]
                    continue

            # coin 사용해서 안되면 게임 종료           
            return step

        else: # 내 카드의 합이 n+1이 되는 경우
            del my_cards[c2]
            del my_cards[c1]
            
    return step + 1

        
def make_target(target, cards):
    # cards 에서 2개 뽑아 target 만들기 
    cards.sort()
    left = 0
    right = len(cards) - 1
    while left < right:
        total = cards[left] + cards[right]
        if target == total:
            return left, right
        
        if target > total:
            left += 1
        else:
            right -= 1
            
    return -1, -1

def make_target2(target, cards, keep_cards):
    # cards 중 1장, kee_cards 중 1장 뽑아 target 만들기 
    keep_cards.sort()
    for i in range(len(cards)):
        x = find_target(target-cards[i], keep_cards)
        if x > -1:
            return i, x
        
    return -1, -1

def find_target(target, cards):
    left = 0
    right = len(cards)-1

    while left <= right:
        mid = (left + right) // 2
        if target < cards[mid]:
            right = mid - 1
        elif target > cards[mid]:
            left = mid + 1
        else:
            return mid
    
    return  -1

