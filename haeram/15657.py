from sys import stdin

"""
template 3
"""

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

idx = [0] * m


def print_cur(array):
    ans = []

    for a in array:
        ans.append(arr[a])

    print(*ans)


def recur(cur, start):
    if cur == m:
        # print
        print_cur(idx)
        return

    for i in range(start, n):
        idx[cur] = i
        recur(cur + 1, i)


recur(0, 0)
