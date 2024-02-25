from sys import stdin

"""
"""
arr = [list(map(int, stdin.readline().split())) for _ in range(3)]
cand = [[0] * 3 for _ in range(3)]
visited = [0] * 10

ans = 81


def check(arr):  # 모두 합이 같은지 확인 (가로세로, 대각선)
    init = sum(arr[0])

    # 가로 합 체크
    for i in range(3):
        total = 0
        for j in range(3):
            total += arr[i][j]

        if total != init:
            return False

    # 세로 합 체크
    for i in range(3):
        total = 0
        for j in range(3):
            total += arr[j][i]

        if total != init:
            return False

    # 대각선 체크
    if arr[0][0] + arr[1][1] + arr[2][2] != init:
        return False
    if arr[0][2] + arr[1][1] + arr[2][0] != init:
        return False

    return True


def recur(x, y, cost):
    global ans

    # y가 끝까지 가면, 다음 줄로 변경
    if y == 3:
        x += 1
        y = 0

    # 줄을 바꿨는데 마지막이었다면 모두 순회한 것임
    if x == 3:
        if check(cand):
            # 합이 모두 같다면 정답 업데이트
            ans = min(ans, cost)

        return

    for i in range(1, 10):
        if visited[i]:
            continue

        visited[i] = 1
        cand[x][y] = i
        recur(x, y + 1, cost + abs(arr[x][y] - i))

        visited[i] = 0


recur(0, 0, 0)
print(ans)
