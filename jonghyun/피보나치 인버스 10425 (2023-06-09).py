# from decimal import Decimal

def bisect(target) :
    global dp
    en = len(dp)

    st = 0
    mid = 0
    while st <= en :

        mid = (st + en) // 2
        if target > dp[mid] :
            st = mid + 1
        elif target == dp[mid] :
            return mid
        else :
            en = mid - 1
        
    return None


INF = 10**22000
global dp 
dp = []

dp.append(0)
dp.append(1)

i = 2
while True :
    dp.append(dp[i-1] + dp[i-2])
    i += 1
    if dp[-1] > INF :
        break


T = int(input())

for _ in range(T) :
    print( bisect( int(input()) ) )