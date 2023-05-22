from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    h, w, n = map(int, stdin.readline().split())

    room = n // h + 1
    if n % h == 0:
        floor = h
        room -= 1
    else:
        floor = n % h

    print(floor * 100 + room)
