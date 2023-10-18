
c, r = list(map(int, input().split()))

dp = [[[0,0,0,0] for j in range(c)] for i in range(r)]


for i in range(r):
    dp[i][0] = [0,1,0,0]

for j in range(c):
    dp[0][j] = [1,0,0,0]

# print(*dp, sep = "\n")

for i in range(1, r):
    for j in range(1, c):
        dp[i][j][3] = dp[i-1][j][0]
        dp[i][j][2] = dp[i][j-1][1]
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][3]

print(sum(dp[r-1][c-1]) % 100_000)