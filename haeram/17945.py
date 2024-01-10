from sys import stdin

a, b = map(int, stdin.readline().split())

ans = []
for i in range(-1000, 1001):
    if (i*i + 2*a*i + b == 0):
        ans.append(i)

print(*ans)
