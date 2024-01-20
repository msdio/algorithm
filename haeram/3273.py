from sys import stdin

"""
1. 완전탐색을 고려해본다.
2. 시간복잡도가 10^6 * 10^6 이다. 절대 안됨.
3. 투 포인터로 하면 10^6으로 되겠다.
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())

arr.sort()

# two pointer
start = 0
end = n - 1

ans = 0
while start < end:
    cur_sum = arr[start] + arr[end]

    if cur_sum == x:
        ans += 1
        start += 1
        end -= 1
        continue

    if cur_sum > x:
        end -= 1
        continue

    if cur_sum < x:
        start += 1
        continue

print(ans)
