from sys import stdin

n = int(stdin.readline())

"""
넘을 수 없는 조건을 따져보자

1. 연속된게 2개 초과일 때
2. 1번에서 2가 2개 이상일 때

현재 위치, 선인장 연속 개수, 1 연속 개수, 2 연속 개수
이렇게 넘기면 된다.
"""

# ans = 0


# def recur(cur, cactus, cnt1, cnt2):
#     global ans

#     if cnt1 > 2 or cnt2 > 1:
#         return

#     if cur == n:
#         if cactus:  # 선인장이 하나는 있어야 한다.
#             ans += 1

#         return

#     recur(cur + 1, cactus, 0, 0)  # 1, 2 둘 다 안심었을 경우
#     recur(cur + 1, cactus, cnt1 + 1, 0)  # 1짜리 심었을 경우
#     recur(cur + 1, True, cnt1 + 1, cnt2 + 1)  # 2짜리 심었을 경우


# recur(1, 0, 0, 0)
# print(ans)


"""
return 방식으로 변경
"""


# def recur(cur, cactus, cnt1, cnt2):
#     if cnt1 > 2 or cnt2 > 1:
#         return 0

#     if cur == n:
#         if cactus:
#             return 1
#         else:
#             return 0

#     return (
#         recur(cur + 1, cactus, 0, 0)
#         + recur(cur + 1, cactus, cnt1 + 1, 0)
#         + recur(cur + 1, True, cnt1 + 1, cnt2 + 1)
#     )


# print(recur(1, 0, 0, 0))

"""
메모이제이션
1은 최대 3개, 2는 최대 2개, cactus값은 최대 2개
"""
DIVIER = 1_000_000_007
dp = [[[[-1, -1] for _ in range(3)] for _ in range(2)] for _ in range(n)]


def recur(cur, cactus, cnt1, cnt2):
    if cnt1 > 2 or cnt2 > 1:
        return 0

    if cur == n:
        if cactus:
            return 1
        else:
            return 0

    if dp[cur][cactus][cnt1][cnt2] != -1:
        return dp[cur][cactus][cnt1][cnt2]

    dp[cur][cactus][cnt1][cnt2] = (
        recur(cur + 1, cactus, 0, 0)
        + recur(cur + 1, cactus, cnt1 + 1, 0)
        + recur(cur + 1, True, cnt1 + 1, cnt2 + 1)
    ) % DIVIER
    return dp[cur][cactus][cnt1][cnt2]


print(recur(1, 0, 0, 0))
