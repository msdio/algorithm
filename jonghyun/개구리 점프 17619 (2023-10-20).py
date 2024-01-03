N, Q = list(map(int, input().split()))

li = []
for i in range(N):
    x1, x2, y = list(map(int, input().split()))
    li.append((x1, x2, y, i))

print(li)

for _ in range(Q):
    a1, a2 = list(map(int, input().split()))
