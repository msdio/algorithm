from sys import stdin

a, b, c, d, e, f = map(int, stdin.readline().split())

ans = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c and d*x + e*y == f):
            ans = [x, y]
            break

    if (ans != []):
        break

print(*ans)
