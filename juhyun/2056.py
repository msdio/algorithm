import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

            
dp = [0]*(N+1)
for i in range(N):
    income = list(map(int,input().split()))
    time = income[0]
    x = income[1]
    i = i+1
    dp[i] = time
    if x == 0:
        graph[i].append([i,time,0])
        continue
    for next_node in income[2:]:
        
        graph[i].append([i,time,next_node])


for i in range(1,N+1):
    time = 0
    for a, b, c in graph[i]:
        time = max(time,dp[c])
    dp[i] += time
print(max(dp))
