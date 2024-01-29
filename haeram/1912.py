from sys import stdin

'''
완탐을 어떻게 할 수 있을까..
최대값을 구하고 앞, 뒤로 가면서 최대값을 계속 업데이트 하면 된다.
그러면 O(N)(최대값 찾기) * O(2N)(앞뒤로 확인) 이니까 시간 안에 되지 않는다.

그러면 누적합을 구하고 누적합의 최대값 - 누적합의 최소값을 하면 되려나?

누적합으로 구하는건 안될 것 같다.
증감 여부를 매번 확인할 수가 없는데
'''

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split())) + [0]

dp = [0]*n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))
