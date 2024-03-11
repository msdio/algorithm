from sys import stdin

n, k = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

"""
이번 물건을 담는 경우, 안 담는 경우
"""

ans = 0


def recur(cur, weight, total):
    global ans

    if weight > k:
        return

    if cur == n:
        ans = max(ans, total)
        return

    recur(cur + 1, weight + arr[cur][0], total + arr[cur][1])  # 이번 물건을 선택
    recur(cur + 1, weight, total)  # 이번 물건을 선택하지 않음


recur(0, 0, 0)
print(ans)


"""
리턴하는 방식으로 변경
"""
