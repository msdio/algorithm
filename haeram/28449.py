from sys import stdin

'''
완탐이면 그냥 O(NM) 이다.

두 배열을 정렬하고, b배열의 각 원소마다 a 배열을 탐색할거다.
b의 원소를 기준으로 a에서 찾고

왼쪽에 있는 애들은 내가 이기는 애들이고
오른쪽에 있는 애들은 내가 지는 애들이다.

lower bound, upper bound 사용하면 될듯

혹시 일치하는 애들을 찾으면 무승부가 1번 있는거다.
코딩 실력이 같은 참가자가 있을테니 무승부가 1번 이상 있을 수 있다.
'''

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

a.sort()

# 부분합 구하기
psum = [0]*(n+1)
psum[0] = a[0]
for i in range(1, n):
    psum[i] = psum[i-1] + a[i]


def lower_bound(target):
    start = 0
    end = n-1
    idx = -1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] >= target:
            idx = mid
            end = mid-1
        else:
            start = mid+1

    return n if idx == -1 else idx


def upper_bound(target):
    start = 0
    end = n-1
    idx = -1

    while start <= end:
        mid = (start+end) // 2

        if a[mid] <= target:
            idx = mid
            start = mid+1
        else:
            end = mid-1

    return idx+1


# B팀 기준
win = 0
lose = 0
draw = 0

for i in range(m):
    left = lower_bound(b[i])
    right = upper_bound(b[i])

    if left <= right:
        lose += n-right
        win += left
        draw += right-left

print(lose, win, draw)
