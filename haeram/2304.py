from sys import stdin

n = int(stdin.readline())
pillars = [list(map(int, stdin.readline().split())) for _ in range(n)]

pillars.sort(key=lambda x: x[0])

from_left = []
from_right = []
psum_left = [0 for _ in range(n-1)]
psum_right = [0 for _ in range(n-1)]

# left
cur_height = pillars[0][1]
for i in range(1, n):
    [l, h] = pillars[i]

    from_left.append(cur_height * (l - pillars[i-1][0]))

    if (h > cur_height):
        cur_height = h

psum_left[0] = from_left[0]
for i in range(1, n-1):
    psum_left[i] = psum_left[i-1] + from_left[i]

# right
cur_height = pillars[-1][1]
for i in range(n-1, 0, -1):
    [l, h] = pillars[i]

    if (h > cur_height):
        cur_height = h

    from_right.insert(0, (cur_height * (l - pillars[i-1][0])))


psum_right[-1] = from_right[-1]
for i in range(n-2, 0, -1):
    psum_right[i-1] = psum_right[i] + from_right[i]


print(from_left)
print(psum_left)

print(from_right)
print(psum_right)
