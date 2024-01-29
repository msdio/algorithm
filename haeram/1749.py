from sys import stdin

"""
누적합으로 (i, j)까지의 합을 구하고,

2차원 배열에서 최대값을 구한 다음
최소값도 찾아서 
그 두개를 뺀다.

근데 (0, 0)부터 시작하는게 아니니까, 
매번 누적합을 계산할 때에 최대값을 업데이트 해줘야 한다.

(u, v) ~ (i, j) 까지의 합을 계속 확인하면 된다.

값이 -10000부터 시작하니까 초기값은 -10001
"""

# n, m = map(int, stdin.readline().split())
# arr = []
# for _ in range(n):
#     row = list(map(int, stdin.readline().split()))
#     arr.append(row)

# dp = [[0] * m for _ in range(n)]
# dp[0][0] = arr[0][0]

# # initialize dp array
# for i in range(1, m):
#     dp[0][i] = dp[0][i - 1] + arr[0][i]

# for i in range(1, n):
#     dp[i][0] = dp[i - 1][0] + arr[i][0]

# # calculate dp
# ans = -10001
# for i in range(1, n):
#     for j in range(1, m):
#         dp[i][j] = arr[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

#         # update max value(which is answer)
#         for u in range(1, i):
#             for v in range(1, j):
#                 ans = max(
#                     ans, dp[i][j] - dp[i][v - 1] - dp[u - 1][j] + dp[u - 1][v - 1]
#                 )

# print(ans)

"""
이렇게 하니까 로직은 맞은 것 같은데... 0~1까지는 검사를 못한다.
그래서 원래 배열의 0열과 0행에 0을 추가해주고 0부터 검사를 해야할 것 같다.

배열 맨 앞에 0을 넣어주면 0번째 row, column을 따로 계산해주는 것도 없어지겠다.
"""

n, m = map(int, stdin.readline().split())
arr = [[0] * (m + 1)]
for _ in range(n):
    row = [0] + list(map(int, stdin.readline().split()))
    arr.append(row)


ans = -10001
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

        # update max value at range (u+1, v+1)~(i, j) (which is answer)
        for u in range(i):
            for v in range(j):
                ans = max(ans, dp[i][j] - dp[i][v] - dp[u][j] + dp[u][v])

print(ans)
