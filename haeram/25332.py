from sys import stdin

"""
누적합이 같은 지점을 찾으면 된다.
0번째부터의 누적합을 비교하는건 쉽다. 근데 시작지점이 0번이 아닌 경우가 문제다.

i부터 j까지의 합을 비교한다고 하면
a[i]-a[j] == b[i]-b[j] 가 되어야 함
a[i]-b[i] == a[j]-b[j] 로 바꿀 수 있음
"""

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
b = [0] + list(map(int, stdin.readline().split()))

# 누적합
psum_a = [0] * (n + 1)
psum_b = [0] * (n + 1)

ans = 0
dict = {}
for i in range(1, n + 1):
    psum_a[i] = psum_a[i - 1] + a[i]
    psum_b[i] = psum_b[i - 1] + b[i]

    if psum_a[i] == psum_b[i]:  # 누적합이 같으면 카운트
        ans += 1

    if psum_a[i] - psum_b[i] in dict:
        ans += dict[psum_a[i] - psum_b[i]]
        dict[psum_a[i] - psum_b[i]] += 1
    else:
        dict[psum_a[i] - psum_b[i]] = 1

print(ans)
