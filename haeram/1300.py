from sys import stdin

'''
완탐으로 하면 n^2 이기 때문에 안된다.

정렬한다음 lower_bound 쓰고 싶어도 정렬하는거 자체까지가 n^2다 
흠...

b[k]를 구하려면 나보다 작은게 k개 존재하면 된다.
그럼 배열에서 나보다 작은게 몇 개인지를 셀 수 있으면

최소 값 1,
최대 값 n*n로 놓고

지금 값보다 작은게 K보다 많다면 -> 값을 더 줄이면 된다.
지금 값보다 작은게 k보다 적다면 -> 값을 더 키우면 된다.

그럼 배열에서 나보다 작은 애가 몇 개 있는지 어떻게 세는가?

1*1 1*2 1*3 1*4 1*5 ... 1*n
2*1 2*2 2*3 2*4 2*5 ... 2*n
3*1 3*2 3*3 3*4 3*5 ... 3*n
...
n*1 n*2 n*3 n*4 n*5 ... n*n

꼴이니까
각 라인에서 k보다 작거나 같은 애들의 개수는 
i 행에서 기준으로 하면 k를 i로 나누면 각 행이 1, 2, 3, 4, ... , k가 된다.
그래서 k보다 작거나 같은 애들의 개수는 k//i 값과 같다.

아 근데 n보다 커질 수는 없으니까 min(n, k//i) 겠다.
'''

n = int(stdin.readline())
k = int(stdin.readline())


def count_smaller(target):  # 배열에 나 이하인 수가 몇개인지 센다.
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, target // i)

    return cnt


start = 0
end = n*n

while start <= end:
    mid = (start+end) // 2

    cand = count_smaller(mid)

    if cand < k:
        start = mid+1
    else:
        end = mid-1

print(start)
