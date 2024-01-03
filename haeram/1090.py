from sys import stdin

n = int(stdin.readline())
checker_x = []
checker_y = []

for i in range(n):
    x, y = map(int, stdin.readline().split())

    checker_x.append(x)
    checker_y.append(y)

set_x = list(set(checker_x))
set_y = list(set(checker_y))

cands = []
for i in range(len(set_x)):
    for j in range(len(set_y)):
        cands.append((set_x[i], set_y[j]))

ans = [10**6 for _ in range(n)]

for cand in cands:
    distance_x = [abs(checker_x[i] - cand[0]) for i in range(n)]
    distance_y = [abs(checker_y[i] - cand[1]) for i in range(n)]

    distances = [distance_x[i] + distance_y[i] for i in range(n)]

    psum = sorted(distances).copy()
    for i in range(1, n):
        psum[i] = psum[i-1] + distances[i]

    for i in range(n):
        if (ans[i] > psum[i]):
            ans[i] = psum[i]

print(*ans)
