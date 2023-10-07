from collections import deque

N, M = list(map(int, input().split()))

fan_in = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
dp = [1 for _ in range(N+1)]
for _ in range(M):
    A, B = list(map(int, input().split()))
    graph[A].append(B)
    fan_in[B] += 1


dq = deque()
for i in range(len(fan_in)):
    if i == 0:
        continue
    if fan_in[i] == 0:
        dq.append(i)
while dq:
    pop = dq.popleft()
    for i in graph[pop]:
        fan_in[i] -= 1
        if fan_in[i] == 0:
            dq.append(i)
            dp[i] = max(dp[pop] +1, dp[i])

print(*dp[1:], sep=" ")
