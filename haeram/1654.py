from sys import stdin

'''
랜선 길이 h로 잘랐을 때 N개 이상 되는지 확인
되면 정답 업데이트
'''

k, n = map(int, stdin.readline().split())
lines = [int(stdin.readline()) for _ in range(k)]

start = 1
end = max(lines)


def cal(h):
    cnt = 0

    for line in lines:
        cnt += line // h

    return cnt


while start <= end:
    mid = (start+end) // 2

    cand = cal(mid)

    if cand < n:  # 랜선 개수가 모자라면 더 짧게 잘라야 한다.
        end = mid-1
    else:  # 더 길게 자를 수 없는지 확인한다.
        start = mid+1


print(end)
