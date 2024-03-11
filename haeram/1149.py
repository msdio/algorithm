from sys import stdin

"""
이전에 고른것 제외하고 모두 고를 수 있다.
"""

# n = int(stdin.readline())
# arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

# ans = 1 << 60


# def recur(cur, cost, prev):
#     global ans

#     if cur == n:
#         ans = min(ans, cost)
#         return

#     for i in range(3):
#         if i == prev:  # 이전에 고른건 패스
#             continue

#         recur(cur + 1, cost + arr[cur][i], i)


# recur(0, 0, -1)
# print(ans)

"""
여기에 메모이제이션 추가
"""

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[-1] * 3 for i in range(n)]

ans = 1 << 60


def recur(cur, prev):
    if cur == n:
        return 0

    if dp[cur][prev] != -1:
        return dp[cur][prev]

    ret = 1 << 60
    for i in range(3):
        if i == prev:
            continue

        ret = min(
            ret, recur(cur + 1, i) + arr[cur][i]
        )  # 다음 줄의 최솟값 + 이번거 골랐을 때 값

    dp[cur][prev] = ret
    return ret


print(recur(0, -1))
