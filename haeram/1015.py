from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr_idx = []
for i in range(n):
    arr_idx.append([arr[i], i])

arr_idx.sort(key=lambda x: x[0])

idx = [0] * n
for i in range(n):
    idx[arr_idx[i][1]] = i

print(*idx)
