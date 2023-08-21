from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [i for i in range(1, n + 1)]

for _ in range(m):
    x, y = map(int, stdin.readline().split())

    temp = arr[x - 1]
    arr[x - 1] = arr[y - 1]
    arr[y - 1] = temp

print(*arr)
