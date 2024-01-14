from sys import stdin
from itertools import combinations

'''
100C2로 모든 경우에 다 구해보면 됨
'''
n = int(stdin.readline())


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


for _ in range(n):
    arr = list(map(int, stdin.readline().split()))

    cands = combinations(arr, 2)

    ans = 0
    for cand in cands:
        cur = gcd(cand[0], cand[1])

        ans = max(ans, cur)

    print(ans)
