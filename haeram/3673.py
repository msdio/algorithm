from sys import stdin

"""
https://www.acmicpc.net/problem/2015 와 같은 문제같다.

배열의 부분합을 구하고,
나눠 떨어지려면 우선
1. 본인이 나눠떨어지거나
2. (부분합 원소 - 부분합 원소) 가 나눠떨어지거나

2번이 되려면 현재 i번째라고 했을 때 [0, i)에서 d-i의 개수를 세면 된다.
arr[i]==0 인 경우에는 0의 개수를 세면 된다.
"""

c = int(stdin.readline())

for _ in range(c):
    d, n = map(int, stdin.readline().split())
    arr = [0] + list(map(int, stdin.readline().split()))

    dict = {}
    ans = 0

    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = (psum[i - 1] + arr[i]) % d

        # 만약 나눠떨어지면 [0, i] 부분수열도 정답
        if psum[i] == 0:
            ans += 1

        # psum[i] == 0 인 경우를 고려하기 위해 d로 모듈러 해줌
        target = (d - psum[i]) % d
        if target in dict:
            ans += dict[target]
            dict[target] += 1
        else:
            dict[target] = 1

    print(ans)
