import sys
input= sys.stdin.readline

N,M = map(int,input().split())

min_p = 2147000000
min_o = 2147000000

for _ in range(M):
    package, once = map(int,input().split())
    min_p = min(min_p, package) # 6개
    min_o = min(min_o, once) # 1개



dp = [2147000000]*(N+10)

res = 1000*M
def DFS(bought_count,money):
    global res
    if bought_count >= N+9:
        return
    if dp[bought_count] <= money:
        return
    else:
        dp[bought_count] = money

    DFS(bought_count + 6, money + min_p)
    DFS(bought_count + 1, money + min_o)

DFS(0,0)
print(min(dp[N:]))



