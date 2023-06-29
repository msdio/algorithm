from itertools import permutations


def move_price(x, y) :
    if x == 0 :
        return 2

    if x == y :
        return 1
    elif abs(x - y) == 2:
        return 4
    else :
        return 3


    

INF = 0xFFFFFFFF
cases = []
for i in permutations([0,1,2,3,4], 2):
    cases.append(i)

dp = [ [[INF for j in range(5)] for i in range(5)] for _ in range(10)]

dp[0][0][0] = 0

li = list(map(int, input().split()))
temp = 0
for index, value in enumerate(li) :
    if value == 0 :
        break
    for i in range(5) :
        for j in range(5) :
            if value == i :
                continue
            dp[index + 1][i][value] = min( dp[index + 1][i][value], dp[index][i][j] + move_price(j, value) )
    
    for i in range(5) :
        for j in range(5) :
            if value == j :
                continue
            dp[index + 1][value][j] = min( dp[index + 1][value][j], dp[index][i][j] + move_price(i, value) )

print(dp)

en = len(li) -1
t = li[-2]

ans = INF

for i in range(5) :
    ans = min(dp[en][t][i], ans)
    
for i in range(5) :
    ans = min(dp[en][i][t], ans)

print(ans)
 