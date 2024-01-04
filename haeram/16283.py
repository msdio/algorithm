from sys import stdin

a, b, n, w = map(int, stdin.readline().split())

cnt = 0
sheep, goat = 0, 0
for i in range(1, 1001):
    for j in range(1, 1001):
        if (i+j == n and a*i+b*j == w):
            cnt += 1
            sheep = i
            goat = j

if (sheep < 1 or goat < 1 or cnt > 1):
    print(-1)
else:
    print(sheep, goat)
