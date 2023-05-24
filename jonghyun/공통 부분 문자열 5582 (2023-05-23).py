
def get_long_str(s1, s2) :

    m = len(s1)
    n = len(s2)

    size = 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1) :
        for j in range(1, n + 1) :
            if s2[j - 1] == s1[i - 1] :
                dp[i][j] = dp[i-1][j-1] + 1
                size = max(dp[i][j], size)
    
    # for i in dp :
        # print(i)
    return size




def solution() :
    str1 = list(input())
    str2 = list(input())

    print(get_long_str(str1, str2))

solution()

'''
ABRACADABRA
ECADADABRBCRDARA
'''