from sys import stdin

"""
맨 왼쪽부터 시작해서 최대값으로 계속 업데이트 하고
맨 오른쪽에서 시작해서 최대값으로 계속 업데이트 하고
두 배열 비교하면서 최소값으로 업데이트 한다.

그리고 왼쪽부터 돌면서 (만든배열) - (현재높이) 를 하면 된다.
"""

h, w = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

from_left = [0] * (w)
from_right = [0] * (w)

from_left[0] = arr[0]
from_right[w - 1] = arr[w - 1]

for i in range(1, w):
    from_left[i] = max(from_left[i - 1], arr[i])

for i in range(w - 2, -1, -1):
    from_right[i] = max(from_right[i + 1], arr[i])

heights = []
for i in range(w):
    heights.append(min(from_left[i], from_right[i]))


ans = 0
for i in range(w):
    ans += max(heights[i] - arr[i], 0)

print(ans)
