from sys import stdin

"""
template 2
"""

n, m = map(int, stdin.readline().split())

arr = [0] * m


def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(n):
        arr[cur] = i + 1

        recur(cur + 1)


recur(0)
