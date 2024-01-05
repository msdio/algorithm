from sys import stdin

num = list(map(int, stdin.readline().split()))

for i in range(4, 10**6):
    cnt = 0
    for n in num:
        if (i % n == 0):
            cnt += 1

    if (cnt >= 3):
        print(i)
        break
