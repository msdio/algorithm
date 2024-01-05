from sys import stdin
from itertools import combinations

arr = []
for _ in range(9):
    n = int(stdin.readline())
    arr.append(n)

cands = list(combinations(arr, 7))

ans = []
for cand in cands:
    if (sum(cand) == 100):
        ans = sorted(cand)
        break

for a in ans:
    print(a)
