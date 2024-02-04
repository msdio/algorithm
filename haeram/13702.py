from sys import stdin

'''
완탐을 하려면
용량의 최대값부터 시작해서 1씩 내리면서 N명한테 분배가 되는지 확인해야 한다.
그러면 O(2^31)이라는 어마무시한 시간복잡도가 된다.

1명한테 주는 막걸리 용량을 h라고 했을 때,
이걸로 n개를 만들 수 있는지 보면 된다. (이분탐색)
'''

n, k = map(int, stdin.readline().split())
pots = [int(stdin.readline()) for _ in range(n)]


def cal(height):
    people = 0

    for pot in pots:
        people += pot // height

    return people


start = 1  # n<=k 이므로 최소값은 1이다.
end = max(pots)


while start <= end:
    mid = (start+end) // 2

    cand = cal(mid)

    if cand < k:
        end = mid-1
    else:
        start = mid+1

print(end)
