from sys import stdin

"""
https://www.acmicpc.net/problem/3673 과 비슷한 문제같다.

배열을 더하는 모든 경우를 고려하면서 t와 비교하면
시간복잡도가 O(n^2 * m^2) 이다.

배열 a와 b의 누적합을 모두 구해놓는다.
또 각 경우에 나오는 숫자들도 dictionary에 저장해놓는다.
근데 중요한건 배열 자체도 우선 dictionary에 넣어야 하겠다.

그 다음 누적합을 다시 순회하면서 t - arr[i] 의 개수를 더한다.

겹치면 안되니까 a 기준으로, b에서 t-arr_A[i] 개수를 세면 되겠다.

이렇게 하면 b의 누적합은 구할 필요가 없다.
"""

t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

dict = {}
# update combinations of A and dictionary
for i in range(n):
    for j in range(i, n):
        cur_sum = sum(a[i : j + 1])

        if cur_sum in dict:
            dict[cur_sum] += 1
        else:
            dict[cur_sum] = 1

# 이제 b의 합이 되는 경우의 수를 모두 구하고,
# 각 경우에 대해서 dict[t-b_sum]의 개수를 찾아 더해주면 된다.
ans = 0
for i in range(m):
    for j in range(i, m):
        cand = sum(b[i : j + 1])

        if (t - cand) in dict:
            ans += dict[t - cand]

print(ans)
