import sys
from sys import stdin
from itertools import combinations

"""
모든 조합을 고려하면 되는거 아닌가?
그래도 시간이 되지 않나
"""

n, k = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

if k <= 1:
    print(0)
    sys.exit(0)


cands = list(combinations([i for i in range(n)], k))


def cal(cur):
    sum = 0
    points = combinations(cur, 2)

    for point in points:
        x, y = point
        sum += arr[x][y]

    return sum


ans = -1 * 10**5
for cand in cands:
    ans = max(ans, cal(cand))

print(ans)
