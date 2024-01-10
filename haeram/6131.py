from sys import stdin

n = int(stdin.readline())

cnt = 0
for b in range(1, 501):
    for a in range(b, 501):
        if (a*a == b*b + n):
            cnt += 1
            break

print(cnt)
