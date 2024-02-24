from sys import stdin

"""
쓴 경우, 안 쓴 경우를 구분해야 한다.
매 번 diff 값을 업데이트하면 된다.
"""

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for i in range(n)]

ans = 10**10


def recur(cur, cnt, sour, bitter):
    global ans

    if cur == n:
        if cnt != 0 and abs(sour - bitter) < ans:
            ans = abs(sour - bitter)

        return

    recur(cur + 1, cnt + 1, sour * arr[cur][0], bitter + arr[cur][1])  # 사용하는 경우
    recur(cur + 1, cnt, sour, bitter)  # 안 쓰는 경우


recur(0, 0, 1, 0)
print(ans)
