from sys import stdin

"""
우선 밑장빼기를 안했을 때를 구해본다.

그리고 매번 밑장을 뺐을 때 최대값이 커지는지 확인하면 된다.
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

# 원래 합 구하기
original = 0
for i in range(0, n, 2):
    original += arr[i]

ans = original
cur_max = original  # 밑장을 안 뺐을 때부터 시작해서, 밑장을 빼면 값이 더 커지는지 확인
for i in range(n - 1, -1, -2):
    cur_max += arr[i]
    cur_max -= arr[i - 1]
    ans = max(ans, cur_max)

cur_max = original
for i in range(n - 2, 0, -2):
    cur_max -= arr[i]
    cur_max += arr[i - 1]
    ans = max(ans, cur_max)

print(ans)
