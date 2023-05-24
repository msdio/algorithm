def solution() :

    n = int(input())
    students = list(map(int, input().split()))
    dp = [0] * (len(students)+1)

    
    for i in range(1, len(students) + 1) :
        for j in range(1, i+1) :
            dp[i] = max(dp[i], dp[i-j] + (max(students[i-j:i]) - min(students[i-j:i])))

    print(dp[-1])


solution()


'''
10
2 5 7 1 3 4 8 6 9 3
'''