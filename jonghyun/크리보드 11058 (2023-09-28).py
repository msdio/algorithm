N=int(input())
dp = [i for i in range(101)]
for i in range(4, N+1):
    for j in range(0, i-4):
        dp[i] = max(dp[i-3-j]*(j+2), dp[i])
print(dp[N])