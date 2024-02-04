from sys import stdin

'''
nCc로 집의 경우를 모두 구하고
각 경우에 거리 최대값을 구하면 n^2 * n 으로 해결된다.

시간복잡도가 택도 없다.

우선 집을 좌표 순으로 정렬하고
거리가 최대가 되려면 처음과 끝에는 무조건 공유기가 있어야 한다.

거리를 D로 했을 때, n개를 설치할 수 있는지 확인하면 된다.
n개보다 더 많이 넣을 수 있다면 계속 거리를 더 키우면 됨. (이분탐색)
'''

n, c = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]

arr.sort()


def cal(distance):
    cnt = 1
    last = arr[0]

    for i in range(n):
        if arr[i] < last + distance:
            continue

        cnt += 1
        last = arr[i]

    return cnt


start = 2
end = arr[-1] - arr[0]

while start <= end:
    mid = (start+end) // 2

    cand = cal(mid)

    if cand >= c:  # 거리를 더 늘릴 수 있음
        start = mid+1
    else:
        end = mid-1

print(end)
