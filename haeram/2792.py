from sys import stdin

'''
최대값이 k인 경우로 보석으로 나누었을 때, 
인원 n명에게 나누어줄 수 있는가?

인원이 n보다 많으면 더 큰 k를 사용해야 한다.
'''

n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(m)]


def divider(arr, target):  # 최대 값이 target인 경우 몇 명에게 나누어 줄 수 있는가?
    cnt = 0

    for a in arr:
        cnt += a // target

        if a % target != 0:
            cnt += 1

    return cnt


start = 1  # 최소 한명한테는 나눠줘야 함 : 이 경우에는 질투가 최대
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    cand = divider(arr, mid)

    if cand > n:  # 최대값을 높여야 함
        start = mid+1
    else:
        end = mid-1

print(start)
