from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    s = stdin.readline().rstrip()

    print(s[0] + s[-1])
