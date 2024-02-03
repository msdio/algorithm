from sys import stdin

'''
만약 완탐 돌리면 n^3으로 된다.
그러면 10^9니까 안됨.

그러면 반복을 하나 줄이면 n^2, 3*n^2로 해결 가능하다. 나머지 하나는 이분탐색으로 찾아보자

예제에서 만약에 a, b가 5, 9로 결정되었다고 하면
a 기준으로 비교하면 c가 [3, 8] 이면 3을 고를텐데
c가 8이 돼야 max - min 값이 더 작아진다.

그래서 a는 b기준으로 고르고, c는 a와 b를 둘 다 고려해서 뽑아야 한다.

b 고르는걸 이분탐색으로 하고
c 고르는걸 완탐으로 하면 되겠다
'''

a, b, c = map(int, stdin.readline().split())
arr_a = list(map(int, stdin.readline().split()))
arr_b = list(map(int, stdin.readline().split()))
arr_c = list(map(int, stdin.readline().split()))

arr_a.sort()
arr_b.sort()
arr_c.sort()


def search(arr, target):  # 가장 차이가 적은 것의 인덱스를 리턴
    start = 0
    end = len(arr)-1

    ret = (start + end) // 2  # 리턴값(가장 가까운 인덱스)
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid-1
        else:
            return mid

        # 최소값 업데이트
        if abs(arr[mid] - target) < abs(arr[ret] - target):
            ret = mid

    return ret


ans = 10**8
for i in range(a):
    selected_b = arr_b[search(arr_b, arr_a[i])]

    # 여기서 c는 a, b를 둘 다 고려해야 한다.
    # 그러면 a에 가까운거 하나랑, b에 가까운거 하나랑 두 개를 가지고
    # 둘 다를 가지고 (최대값)-(최소값)을 구해본 다음 더 작은걸로 정답을 업뎃하면 될듯
    cand_c_with_a = arr_c[search(arr_c, arr_a[i])]
    cand_c_with_b = arr_c[search(arr_c, selected_b)]

    # 이제 이 두개를 가지고 각각 구해본다
    cand_1 = max(arr_a[i], selected_b, cand_c_with_a) - \
        min(arr_a[i], selected_b, cand_c_with_a)
    cand_2 = max(arr_a[i], selected_b, cand_c_with_b) - \
        min(arr_a[i], selected_b, cand_c_with_b)

    # 둘 중 더 작은 값으로 업데이트
    ans = min(ans, cand_1, cand_2)

print(ans)
