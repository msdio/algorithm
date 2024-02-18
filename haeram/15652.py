from sys import stdin

"""
template 3
"""

n, m = map(int, stdin.readline().split())

arr = [0] * m


def recur(cur, start):
    if cur == m:
        print(*arr)
        return

    for i in range(start, n):
        arr[cur] = i + 1
        recur(cur + 1, i)


recur(0, 0)
