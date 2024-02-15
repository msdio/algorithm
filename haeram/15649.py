from sys import stdin

"""
길이 m, 숫자 1~n
template 2
"""

n, m = map(int, stdin.readline().split())
arr = [0] * m
visited = [0] * n


def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        arr[cur] = i + 1
        recur(cur + 1)

        visited[i] = 0


recur(0)
