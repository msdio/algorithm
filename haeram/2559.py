from sys import stdin

'''
완탐으로 하려면 어떻게 할까
시작 지점부터 K번을 다 더하면 된다. 그리고 최솟값 갱신

이러면 N * K = N^2이니까 안된다.

K번째 구간만 보면 되니까
start, end(=start+k) 포인터를 가지고 얘네를 하나씩 뒤로 옮기면 된다.
슬라이딩 윈도우
'''

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

cur = sum(arr[:k])
ans = cur

for i in range(1, n-k+1):
    cur = cur - arr[i-1] + arr[i+k-1]
    ans = max(ans, cur)

print(ans)
