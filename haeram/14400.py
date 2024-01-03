from sys import stdin

n = int(stdin.readline())
stores_x = []
stores_y = []

for i in range(n):
    x, y = map(int, stdin.readline().split())

    stores_x.append(x)
    stores_y.append(y)

ans = 0
ans_x = 0
ans_y = 0
stores_x.sort()
stores_y.sort()


def get_distance(base, array):
    ret = 0

    for a in array:
        ret += abs(base - a)

    return ret


if (len(stores_x) % 2 == 1):
    mid = int((len(stores_x) - 1) / 2)
    ans += get_distance(stores_x[mid], stores_x)
    ans += get_distance(stores_y[mid], stores_y)
else:
    mid = int((len(stores_x)) / 2 - 1)
    ans += get_distance(stores_x[mid], stores_x)
    ans += get_distance(stores_y[mid], stores_y)

print(ans)
