from sys import stdin

"""
재귀 할 때 필요한 변수들
cur, total(전체 합 - s와 같은지 확인), count(센 개수)
"""

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

ans = 0


def recur(cur, cnt, total):
    global ans

    if cur == n:
        if cnt != 0 and total == s:
            ans += 1

        return

    recur(cur + 1, cnt + 1, total + arr[cur])
    recur(cur + 1, cnt, total)


recur(0, 0, 0)
print(ans)
