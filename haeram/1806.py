from sys import stdin

"""
start, end 둘 다 0에서 시작한다.
만약 합이 s보다 작다면 end를 뒤로 민다.
s 이상이라면 ans 값을 업데이트 하고 start를 앞으로 민다.

이렇게 하면 시간복잡도가 O(2n)이다.
"""

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 0
end = 0

ans = 10**6 + 1
partial_sum = arr[0]
while end < n:
    if partial_sum < s:
        end += 1
        if end < n:
            partial_sum += arr[end]
        continue

    if partial_sum >= s:
        ans = min(ans, end - start + 1)
        partial_sum -= arr[start]
        start += 1


if ans == 10**6 + 1:
    print(0)
else:
    print(ans)
