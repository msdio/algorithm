N, K = list(map(int, input().split()))

dp = [[0 for _ in range(K+1)] for _ in range(N)]



for i in range(N):
    walk_min, walk_val, bike_min, bike_val = list(map(int, input().split()))
    if i == 0 :
        for j in range(walk_min, K) :
            dp[i][j] = max(dp[i][j], walk_val)
        for j in range(bike_min, K) :
            dp[i][j] = max(dp[i][j], bike_val)
    else : 
        for j in range(0, K) :
            if dp[i-1][j] == 0 :
                continue
            else :
                if j + walk_min <= K :
                    dp[i][j + walk_min] = max(dp[i][j + walk_min], dp[i-1][j] + walk_val)
                if j + bike_min <= K :
                    dp[i][j + bike_min] = max(dp[i][j + bike_min], dp[i-1][j] + bike_val)

for i in dp :
    print(i)
print(max(dp[-1]))

'''
3 165
50 20 20 10
80 37 30 12
70 25 30 9
'''