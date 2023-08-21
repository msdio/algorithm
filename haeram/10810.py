from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [0] * n

for _ in range(m):
    i, j, k = map(int, stdin.readline().split())

    for v in range(i, j + 1):
        arr[v - 1] = k

print(*arr)
