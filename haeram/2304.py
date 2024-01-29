from sys import stdin

'''
1. 기둥들을 x좌표 순으로 정렬한다.
2. 왼쪽 -> 오른쪽으로 기둥의 max값을 업데이트 한다.
2. 오른쪽 -> 왼쪽으로 똑같이 한다.

2와 3 중 최소값들만으로 구성된 배열을 생성한다.
배열의 총합이 정답
'''

n = int(stdin.readline())

pillars = [0] * 1001
max_x = 0
for _ in range(n):
    l, h = map(int, stdin.readline().split())
    pillars[l] = h
    max_x = max(max_x, l+1)

from_left = [0] * max_x
from_right = [0] * max_x

for i in range(1, max_x):
    from_left[i] = max(from_left[i-1], pillars[i])

for i in range(max_x-1, 0, -1):
    from_right[i-1] = max(from_right[i], pillars[i])


ans = []
for i in range(1, max_x):
    ans.append(min(from_left[i], from_right[i-1]))


print(sum(ans))
