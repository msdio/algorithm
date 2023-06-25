import sys
input = sys.stdin.readline

N = int(input())

dp = [1]*(N+10)
div = 987654321

dp[2] = 1
dp[4]= 2
dp[6] = 5

for i in range(6,N+10,2):
    plus = 0
    for j in range(i-2,0,-2):
        plus += dp[j]*dp[i-j]
        dp[i] = plus

print(dp[N] % div)
