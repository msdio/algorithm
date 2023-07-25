from sys import stdin

k = int(stdin.readline())
n = int(stdin.readline())

start = [chr(i) for i in range(65, 65 + k)]
target = list(stdin.readline().rstrip())
lines = [list(stdin.readline().rstrip()) for _ in range(n)]

# deal with start
for i in range(n):
    if lines[i][0] == "?":
        break

    for j in range(k - 1):
        if lines[i][j] == "-":
            temp = start[j]
            start[j] = start[j + 1]
            start[j + 1] = temp

# deal with target
for i in range(n - 1, -1, -1):
    if lines[i][0] == "?":
        break

    for j in range(k - 1):
        if lines[i][j] == "-":
            temp = target[j]
            target[j] = target[j + 1]
            target[j + 1] = temp

ans = ""
for i in range(k - 1):
    if start[i] == target[i]:
        ans += "*"
    elif start[i] == target[i + 1] and start[i + 1] == target[i]:
        ans += "-"
    elif i != 0 and start[i] == target[i - 1] and start[i - 1] == target[i]:
        ans += "*"
    else:
        ans = "x" * (k - 1)
        break

print(ans)
