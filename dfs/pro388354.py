'''

https://school.programmers.co.kr/learn/courses/30/lessons/388354
- Programmers 388354 홀짝트리 (Lv.3)
- DFS

'''

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def solution(nodes, edges):

    forest = defaultdict(list)
    for n1, n2 in edges:
        forest[n1].append(n2)
        forest[n2].append(n1)

    answer = [0, 0]
    for n in nodes:
        if (n % 2 == 0 and len(forest[n]) % 2 == 0) or (n % 2 != 0 and len(forest[n]) % 2 != 0):
            if get_tree(n, -1, forest):
                answer[0] += 1
        elif (n % 2 == 0 and len(forest[n]) % 2 != 0) or (n % 2 != 0 and len(forest[n]) % 2 == 0):
            if get_reverse_tree(n, -1, forest):
                answer[1] += 1
        
    return answer


def get_tree(cur, root, forest):
    for n in forest[cur]:
        if n == root: continue
        if (n % 2 == 0 and (len(forest[n])-1) % 2 == 0) or (n % 2 != 0 and (len(forest[n])-1) % 2 != 0): continue
        else: return False
        
    for n in forest[cur]:
        if n == root: continue
        if not get_tree(n, cur, forest): return False

    return True

def get_reverse_tree(cur, root, forest):
    for n in forest[cur]:
        if n == root: continue
        if (n % 2 == 0 and (len(forest[n])-1) % 2 != 0) or (n % 2 != 0 and (len(forest[n])-1) % 2 == 0): continue
        else: return False
        
    for n in forest[cur]:
        if n == root: continue
        if not get_reverse_tree(n, cur, forest): return False

    return True
