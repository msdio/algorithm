N = int(input())

string = list(input())
string_reverse = string[:]
string_reverse.reverse()

# print(string, string_reverse)

dp = [[0 for i in range(N+2)] for j in range(N+2)]

for i in range(N) :
    for j in range(N) :
        if string[j] == string_reverse[i]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1-1], dp[i+1][j+1-1])
        else : 
            dp[i+1][j+1] = max(dp[i+1][j+1-1], dp[i+1-1][j+1])

print(N- max(max(dp)))


'''
5
b3aab
'''