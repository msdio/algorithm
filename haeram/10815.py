from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))

arr.sort()


def has_num(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2

        if arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
        else:  # 정답인 경우
            return 1

    return 0


ans = []
for target in targets:
    ans.append(has_num(target))

print(*ans)
