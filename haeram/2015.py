from sys import stdin

'''
완전탐색으로 하려면 2중 for문으로 다 돌면 된다.
이러면 N^2 이니까 안된다.

1 ~ (i-1) 까지 누적합을 하고, 이거랑 i를 더해서 k가 되는 애를 찾으려면
1 ~ (i-1) 중에서 i-k 를 찾으면 된다.
i-k인 애의 인덱스를 j라고 하면
arr[i] - arr[j-1] = k가 되기 때문이다.

이렇게 하려면 매번 계산할 때마다 어떤 수가 나왔는지 종류를 세야 한다.
그리고 배열을 돌면서 arr[i]-k의 개수를 세면 된다.
'''

n, k = map(int, stdin.readline().split())
arr = [0] + list(map(int, stdin.readline().split()))

psum = [0] * (n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i]


dict = {}
ans = 0
for i in range(1, n+1):
    target = psum[i] - k

    if psum[i] == k:
        ans += 1

    if target in dict:
        ans += dict[target]

    if psum[i] in dict:
        dict[psum[i]] += 1
    else:
        dict[psum[i]] = 1

print(ans)
