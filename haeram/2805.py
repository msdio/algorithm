from sys import stdin

'''
완탐하려면
1~나무최대높이까지 1씩 높이면서 다 잘라봐야 하고(높이 10억)
매번 돌면서 나무 개수를 확인해야 한다(n)

높이를 이분탐색으로 바꾼다.
'''

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))


def cal(h):
    cnt = 0

    for tree in trees:
        cnt += max(tree-h, 0)

    return cnt


start = 1
end = max(trees)

while start <= end:
    mid = (start+end)//2

    cand = cal(mid)

    if cand < m:  # 더 짧게 잘라야 한다.
        end = mid - 1
    else:
        start = mid+1

print(end)
