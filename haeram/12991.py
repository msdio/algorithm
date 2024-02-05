from sys import stdin

'''
k번째 수 (https://www.acmicpc.net/problem/1300) 랑 비슷한 방식으로 접근하려 했다

근데 문제가 여기서는 한 행에 들어있는 데이터들이 예상이 됐어서 
나눗셈으로 한번에 처리가 됐었다

배열의 최소값 부터 최대값 까지 이분탐색하는건 될텐데
매 행에서 몇개씩인지 세려면 또 O(N)이 걸린다.

그러면 이것도 이분탐색으로 하면 되나?
최소값을 배열 0번째, 최대값을 배열 n-1번째로 해서 이분탐색 하자
'''

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

a.sort()
b.sort()


def count_smaller(target):  # 나 이하 수들의 개수를 세기
    cnt = 0

    for i in range(n):
        # 여기서도 이분탐색
        start = 0
        end = n-1

        while start <= end:
            mid = (start+end) // 2

            if a[i]*b[mid] > target:
                end = mid-1
            else:
                start = mid+1

        cnt += start

    return cnt


start = a[0]*b[0]
end = a[n-1]*b[n-1]

while start <= end:
    mid = (start+end) // 2

    cand = count_smaller(mid)

    if cand < k:  # 개수가 적으면 k 크기를 키운다.
        start = mid+1
    else:
        end = mid-1

print(start)
