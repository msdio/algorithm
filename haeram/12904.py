# 시간 초과

# from sys import stdin
# import sys

# sys.setrecursionlimit(10**6)


# def appendA(prev: str):
#     return prev + "A"


# def appendB(prev: str):
#     return prev[::-1] + "B"


# s = stdin.readline().rstrip()
# t = stdin.readline().rstrip()
# len_t = len(t)


# def pro(input: str):
#     global t, len_t

#     if len(input) >= len_t:
#         if input == t:
#             print(1)
#             sys.exit(0)

#         return

#     if len(input) < len_t:
#         pro(appendA(input))
#         pro(appendB(input))


# pro(s)
# print(0)

# ----------------------------- #
from sys import stdin

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()
len_s = len(s)


while len_s < len(t):
    if t[-1] == "B":
        t = t[0:-1]
        t = t[::-1]
    elif t[-1] == "A":
        t = t[0:-1]

if s == t:
    print(1)
else:
    print(0)
