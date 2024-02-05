from sys import stdin

'''
완탐을 하려면 어떻게 할까
높이를 1씩 늘려가면서 (10억)
배열에서 높이의 개수를 찾는다.

그 높이로 정사각형을 만들 수 있는지 판단한다.
만들 수 있다면 정답을 그 높이의 제곱으로 업데이트한다.

높이 값 탐색을 줄여야 할 것 같다.
높이를 이분탐색으로 하자.
'''

n = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))


def can_square(h):  # 정사각형을 만들 수 있는가?
    cnt = 0  # count baseline

    for i in range(n):
        if cnt >= h:
            return True

        if heights[i] < h:
            cnt = 0
            continue

        cnt += 1

    return True if cnt >= h else False


start = 1
end = n  # 정사각형이니까 최대 높이는 n이다.

ans = 0
while start <= end:
    mid = (start+end) // 2

    if can_square(mid):
        ans = max(ans, mid**2)
        start = mid+1
    else:
        end = mid-1

print(int(ans**0.5))
