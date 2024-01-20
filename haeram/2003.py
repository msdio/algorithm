from sys import stdin

"""
1. 완탐으로 하면 10^8 이긴 한데... 시간이 0.5초다. 완탐은 안됨.
2. 정렬한 다음
3. 두 번째 for문에서 시작 점을 i로 설정하고, 합이 넘거나 같은 경우 break 하면 되지 않을까?

정렬하면 안된다. 
"""

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

ans = 0
for i in range(n):
    cur_sum = 0

    for j in range(i, n):
        if cur_sum + arr[j] > m:
            break

        if cur_sum + arr[j] == m:
            ans += 1
            break

        cur_sum += arr[j]

print(ans)
