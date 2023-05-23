from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(len(s1)):
    if s1[i] == s2[0]:
        dp[0][i] = 1

for i in range(len(s2)):
    if s2[i] == s1[0]:
        dp[i][0] = 1


ans = 0
for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])

print(ans)
