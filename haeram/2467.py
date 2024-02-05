from sys import stdin

"""
모두 조합할거면 100000C2..? 절대 안된다.

정렬하고 투 포인터를 하려고 고민해봤는데 마땅히 해결책이 될 것 같진 않다.

합이 0이 될라면 크기(절댓값) 순으로 정렬하면 되나?
정렬 하고 내 양옆이랑만 비교하면 되는건가
딱히 반례가 없는 것 같다.
"""

# n = int(stdin.readline())
# arr = list(map(int, stdin.readline().split()))

# arr.sort(key=lambda x: abs(x))

# cur_max = 2 * 10**9
# ans = []
# for i in range(1, n):
#     cand = abs(arr[i-1] + arr[i])

#     if cand < cur_max:
#         ans = [[arr[i-1], arr[i]]]
#         cur_max = cand
#         continue

#     if cand == cur_max:
#         ans.append([arr[i-1], arr[i]])
#         continue

# temp = ans[0]
# temp.sort()

# print(*temp)

#########################################################

"""
용액 배열 정렬한 다음

용액 하나 잡고,
이분탐색 해서 제일 가까운 용액 찾은다음에
정답 업데이트

이렇게 하면 되지 않을까

가까운 용액은 어떻게 찾냐
두 용액을 합쳤을 때 양수면 오른쪽 값들은 답이 될 수 없다 -> end = mid-1
음수면 왼쪽값들은 답이 될 수 없다 -> start = mid+1
"""

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()


def find_liquid(target):  # return current min value and target
    start = 0
    end = n - 1

    cur_min = 2 * 10**9 + 1
    idx = -1
    while start <= end:
        if arr[start] == target:
            start += 1
            continue

        if arr[end] == target:
            end -= 1
            continue

        mid = (start + end) // 2

        diff = target + arr[mid]

        if abs(diff) < cur_min:
            idx = mid
            cur_min = abs(diff)

        if diff == 0:  # 0이면 더 비교할 필요도 없다
            return 0

        if diff < 0:
            start = mid + 1
        else:
            end = mid - 1

    return cur_min, idx


ans = [0, 0]
val = 2 * 10**9 + 1
for liquid in arr:
    cand, idx = find_liquid(liquid)

    if cand < val:
        val = cand
        ans = [liquid, arr[idx]]

print(*sorted(ans))
