from sys import stdin

"""
8 12 의 최대공약수는
(8 12의 최대공약수)와 24의 최대공약수와 같다.
그럼 왼쪽에서부터 구한 약수들 (dp)
오른쪽에서부터 구한 약수들
을 하면

k번째 수를 뺀 애들의 최대공약수는
왼쪽부터 구한 배열에서 k-1번째, 오른쪽에서부터 구한 배열에서 k+1번째
두 수의 최대공약수가 곧 답이다

이걸 최대값으로 업데이트 해주면 된다
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))


def gcd(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2

    return n2


from_left = [0] * (n + 1)
from_right = [0] * (n + 1)

from_left[0] = arr[0]
from_right[n - 1] = arr[n - 1]

for i in range(1, n):
    from_left[i] = gcd(from_left[i - 1], arr[i])

for i in range(n - 2, -1, -1):
    from_right[i] = gcd(from_right[i + 1], arr[i])


# main
ans = [0, 0]
for i in range(n):
    cur = gcd(from_left[i - 1], from_right[i + 1])

    if arr[i] % cur == 0:
        continue

    if ans[0] < cur:
        ans = [cur, arr[i]]

if ans[0] == 0:
    print(-1)
else:
    print(*ans)
