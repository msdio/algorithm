from sys import stdin

"""
완탐으로 하려면 어떻게 할까
매번 start~end 를 다 더하면 된다.
이렇게 하면 10^6 * 10^6 = 10^12 니까 안된다.

그래서 누적합으로하면 O(N)으로 되겠다.
누적합 배열을 psum이라고 하면,
psum[end-1] - psum[start-2] 로 구하면 된다.
근데 만약에 start가 1이면 psum[end-1] 이다. 
"""

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

psum = [0 for _ in range(n)]
psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i - 1] + arr[i]

for _ in range(m):
    start, end = map(int, stdin.readline().split())

    if start == 1:
        print(psum[end - 1])
    else:
        print(psum[end - 1] - psum[start - 2])
