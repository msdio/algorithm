from sys import stdin
# from itertools import combinations

# arr = []
# for _ in range(9):
#     n = int(stdin.readline())
#     arr.append(n)

# cands = list(combinations(arr, 7))

# ans = []
# for cand in cands:
#     if (sum(cand) == 100):
#         ans = sorted(cand)
#         break

# for a in ans:
#     print(a)

'''
투포인터로 접근

1. 전체 합을 구한다.
2. 2개만 빼면 되니까, 덜 뺄지 더 뺄지를 정하면서 포인터 2개를 조절한다.
'''

arr = []
for _ in range(9):
    n = int(stdin.readline())
    arr.append(n)

arr.sort()

# get sum of array
total_sum = sum(arr)

start, end = 0, 8

ans = []
while start < end:
    cur = total_sum - arr[start] - arr[end]
    if cur == 100:
        for i in range(9):
            if i != start and i != end:
                ans.append(arr[i])

        break

    # 더 큰 경우에는 더 빼야 한다.
    if cur > 100:
        start += 1
        continue

    # 더 작은 경우에는 덜 빼야 한다.
    if cur < 100:
        end -= 1
        continue


for a in ans:
    print(a)
