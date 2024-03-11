from sys import stdin
import sys

sys.setrecursionlimit(10**6)

"""
오늘 상담을 하거나, 안하거나
"""

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

ans = 0


# def recur(cur, total):
#     global ans

#     if cur > n:
#         return

#     if cur == n:
#         ans = max(ans, total)
#         return

#     recur(cur + arr[cur][0], total + arr[cur][1])  # 오늘 일 할때
#     recur(cur + 1, total)  # 오늘 일 안할 때


# recur(0, 0)
# print(ans)

"""
return으로 바꾸기
"""


# def recur(cur):
#     if cur > n:
#         return -1 << 60

#     if cur == n:  # 마지막날이면 돈 더 못번다
#         return 0

#     # 오늘 일 하는 것과 안하는 것 중 큰 값을 선택
#     ret = 0
#     ret = max(ret, recur(cur + 1))  # 오늘 일 안할 때
#     ret = max(ret, recur(cur + arr[cur][0]) + arr[cur][1])

#     return ret


# print(recur(0))

"""
메모이제이션
"""

dp = [-1] * n


def recur(cur):
    if cur > n:
        return -1 << 60

    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = max(recur(cur + 1), recur(cur + arr[cur][0]) + arr[cur][1])

    return dp[cur]


print(recur(0))
