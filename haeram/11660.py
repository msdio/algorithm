from sys import stdin

'''
2차원 누적합
'''

n, m = map(int, stdin.readline().split())
arr = [[0] * (n+1)]
for _ in range(n):
    row = [0] + list(map(int, stdin.readline().split()))
    arr.append(row)

psum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        psum[i][j] = arr[i][j] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    ans = psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1]
    print(ans)
