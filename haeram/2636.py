from sys import stdin
from collections import deque

row, col = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(row)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = []
cnt = 0

dq = deque()
dq.append((0, 0))


def bfs(visited):
    global cnt

    visited[0][0] = 1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny < 0 or nx < 0 or ny >= row or nx >= col:
                continue

            if visited[ny][nx]:
                continue

            if arr[ny][nx] == 0:
                visited[ny][nx] = 1
                dq.append((ny, nx))
            elif arr[ny][nx] == 1:
                visited[ny][nx] = 1
                arr[ny][nx] = 0
                cnt += 1

    ans.append(cnt)


time = 0
while 1:

    dq = deque()
    dq.append((0, 0))
    visited = [[0]*col for _ in range(row)]

    bfs(visited)

    if cnt == 0:
        break
    cnt = 0
    time += 1

print(time)
print(ans[-2])
