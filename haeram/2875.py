from sys import stdin

n, m, k = map(int, stdin.readline().split())

n = n-k

ans = 0
for i in range(k+1):
    if (n+i >= 2*(m-i)):
        ans = max(ans, m-i)
    else:
        ans = max(ans, (n+i)//2)

print(ans)
