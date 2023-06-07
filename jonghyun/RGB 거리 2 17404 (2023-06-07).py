n = int(input())
INF = 0xFFFFFFFF
arr = []
min_val = INF

for i in range(n) :
    arr.append(list(map(int, input().split())))


for t in range(3) :
    arr_copy = [t[:] for t in arr]
    arr_copy[-1][t] = INF
    dp = [[0, 0, 0] for _ in range(len(arr_copy))]
    dp[0][t] = arr[0][t]
    dp[0][t-1] = INF
    dp[0][(t+1)%3] = INF

    for i in range(1, len(arr_copy)) :
        for j in range(3) :
            dp[i][j] = arr_copy[i][j] + min(dp[i-1][j-1], dp[i-1][(j+1)%3])

    temp = min(dp[-1])
    min_val = min(temp, min_val)

print(min_val)

