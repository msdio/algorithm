from sys import stdin

"""
완탐으로는 단순하게 하나씩 빼보면서 확인하면 된다.
근데 이렇게 하면 시간복잡도가 O(n^2) 이다.

그럼 그냥 한번에 휩쓸면서 확인해야 한다.
그러면 어떻게 할까
우선 arr[n-1] > arr[n] 이 되는 지점을 찾으면 된다. 
arr[n]을 빼면 되니까.

이 지점의 개수가
1. 0개일때 : 뭘 빼든 상관없으니 n개이다.
2. 2개이상일때 : 1개를 버려서 정렬이 될 수 있는 경우가 없으니 0개이다.
3. 1개일때: 1개 또는 2개이다.
  3-1. arr[n-2] <= arr[n] 이라면 arr[n-1] 을 빼면 되니까 2개이다.
  3-2. 아니라면 1개이다.
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

cnt = 0
point = -1
for i in range(1, n):
    if arr[i - 1] > arr[i]:
        cnt += 1
        point = i

if cnt == 0:
    print(n)
elif cnt >= 2:  # 값이 감소하는 지점이 2개 이상인 경우
    print(0)
else:  # 1개인 경우
    ans = 0
    if point == 1 or arr[point - 2] <= arr[point]:
        ans += 1
    if point == n - 1 or arr[point + 1] >= arr[point - 1]:
        ans += 1

    print(ans)
