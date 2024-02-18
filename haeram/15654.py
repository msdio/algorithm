from sys import stdin

"""
인덱스로 템플릿 2번을 돌리면 된다.
sort 하고 뽑아야 정렬이 자동으로 되겠다
"""

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

idx = [0] * m
visited = [0] * n


def print_cur(array):
    ans = []

    for a in array:
        ans.append(arr[a])

    print(*ans)


def recur(cur):
    if cur == m:
        # print array
        print_cur(idx)

        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        idx[cur] = i

        recur(cur + 1)
        visited[i] = 0


recur(0)
