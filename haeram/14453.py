from sys import stdin

'''
우선 연속하는 것 중에 가장 긴 길이를 찾는다.
그리고 연속한것 이외의 것으로 하나씩 바꿔가면서 앞, 뒤로 최대값을 구한다.
그러면 연속한 배열 찾기 O(N) + 앞 뒤로 한번씩 바꿔보면서 최대값 찾기 2*O(N) 이다.

이걸 구해볼라면 처음부터 지금까지 H, P, S가 몇 개씩 있는지 알아야 한다.
'''

n = int(stdin.readline())
arr = [0]  # 누적합을 구하기 위해 맨 앞에 0을 붙임
for _ in range(n):
    g = stdin.readline().rstrip()
    arr.append(g)

h = [0] * (n+1)
p = [0] * (n+1)
s = [0] * (n+1)

for i in range(1, n+1):
    if arr[i] == 'H':
        h[i] = h[i-1]+1
        p[i] = p[i-1]
        s[i] = s[i-1]
        continue

    if arr[i] == 'P':
        h[i] = h[i-1]
        p[i] = p[i-1]+1
        s[i] = s[i-1]
        continue

    if arr[i] == 'S':
        h[i] = h[i-1]
        p[i] = p[i-1]
        s[i] = s[i-1]+1

ans = 0
for i in range(1, n + 1):
    p_h = p[i - 1] + (h[n] - h[i - 1])
    p_s = p[i - 1] + (s[n] - s[i - 1])
    h_s = h[i - 1] + (s[n] - s[i - 1])
    h_p = h[i - 1] + (p[n] - p[i - 1])
    s_p = s[i - 1] + (p[n] - p[i - 1])
    s_h = s[i - 1] + (h[n] - h[i - 1])

    ans = max(ans, p_h, p_s, h_s, h_p, s_p, s_h)

print(ans)
