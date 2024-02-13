from sys import stdin

"""
완탐하려면?
n명 중에 2명을 고르는 경우의 수를 구하고,
인덱스 차이를 구하면 된다.

nC2 * n 이니까 말도 안된다.

1 줄어드는 것보다 min 값이 커지는게 더 영향이 크다.
그리고 end값이 줄어들면 값이 무조건 작아진다.
근데 start 값이 커지면 커질 건덕지가 생긴다.
start 값만 늘리면서 보면 되는거 아닌가?

그러면 
1. 정렬한다
2. 마지막 포인터(end)는 고정해두고
3. 맨 처음 포인터(start)만 늘려가면서 검사한다.
이렇게 하면 되지 않을까

근데 사이에 한명도 없으면 0이니까 최소 1명은 있어야 한다. 
따라서 n-2까지만 검사하면 된다.
"""

# n = int(stdin.readline())
# power = list(map(int, stdin.readline().split()))

# ans = 0
# for i in range(n - 1):
#     cur = power[i] * (n - i - 1)

#     ans = max(ans, cur)

# print(ans)

"""
문제를 잘못 이해했다..
정렬을 하면 안된다. 지금 있는 상태로 계산해야 함

그러면 포인터 두 개를 두고, 
power[start]와 power[end] 중 더 작은 쪽의 포인터를 옮기면서 계산하면 될 것 같다.

왜냐하면 (사이 개발자 수)가 1 주는 것보다 최소값이 올라가는게 숫자가 더 많이 커지기 때문이다.

사이에 개발자가 한 명은 있어야 하기 때문에, end - start > 1 인 경우까지만 보면 된다.
"""

# n = int(stdin.readline())
# power = list(map(int, stdin.readline().split()))

# ans = 0
# start = 0
# end = n - 1

# ans = 0
# while start + 1 < end:
#     cur = (end - start - 1) * min(power[start], power[end])

#     ans = max(ans, cur)

#     if power[start] > power[end]:
#         end -= 1
#     else:
#         start += 1

# print(ans)

##################################################################

"""
시작점과 끝점을 각각 포인터로 두고
양쪽 점 중 더 작은 값을 안쪽으로 이동시키면서 값을 갱신한다
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

start = 0
end = n - 1

ans = 0
while start < end:
    ans = max(ans, (end - start - 1) * min(arr[start], arr[end]))

    if arr[start] > arr[end]:
        end -= 1
    else:
        start += 1

ans = max(ans, (end - start) * min(arr[start], arr[end]))

print(ans)
