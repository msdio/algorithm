# from sys import stdin

# n = int(stdin.readline())

# points = []
# for _ in range(n):
#     x, y = map(int, stdin.readline().split())

#     points.append([x, y])

# board = [[0] * 101 for _ in range(101)]

# for _ in range(n):
#     for point in points:
#         for i in range(point[1], point[1] + 10):
#             for j in range(point[0], point[0] + 10):
#                 board[i][j] = 1

# cnt = 0
# for b in board:
#     cnt += b.count(1)

# print(cnt)

# ------------------------------------------------------ #

from sys import stdin

n = int(stdin.readline())

points = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())

    points.append([x, y])

s = set()
for _ in range(n):
    for point in points:
        for i in range(point[1], point[1]+10):
            for j in range(point[0], point[0]+10):
                s.add((j, i))

print(len(s))
