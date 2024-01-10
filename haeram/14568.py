from sys import stdin

n = int(stdin.readline())

if (n <= 5):
    print(0)
else:
    cnt = 0

    for i in range(2, n-2, 2):
        cnt += (n-i) // 2 - 1

    print(cnt)
