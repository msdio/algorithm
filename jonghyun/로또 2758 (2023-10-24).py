

T = int(input())
arr = [1,2,4,8,16,32,64,128,256,512,1024]
def getMutiply(n):
    global arr
    return arr[n-1]

for _ in range(T):
    n, m = list(map(int, input().split()))

    dp = [[0 for j in range(m+2)] for i in range(n+2)]
    
    def recursive(depth, num):
        global dp
        # print(dp)
        # print(f"depth, num = {depth, num}")
        if dp[depth][num] != 0:
            return dp[depth][num]        

        if getMutiply(depth) * num > m: return 0
        if depth == 2:
            dp[depth][num] = m - num*2 + 1
            return dp[depth][num]
        
        for i in range(num*2, m+1):
            if getMutiply(depth) * num > m:break
            tmp = recursive(depth - 1, i)
            dp[depth][num] += tmp

        return dp[depth][num]

    answer = 0
    for i in range(1, m+1):
        if getMutiply(n) * i > m:break
        
        answer += recursive(n, i)
    # print(dp)
    print(answer)
