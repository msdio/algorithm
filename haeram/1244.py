from sys import stdin

n = int(stdin.readline())
switches = list(map(int, stdin.readline().split()))
k = int(stdin.readline())


def switch(num):
    return 0 if num == 1 else 1


def boy(idx, arr):
    temp = idx
    length = len(arr)

    while idx <= length:
        arr[idx - 1] = switch(arr[idx - 1])
        idx += temp


def girl(idx, arr):
    length = len(arr)
    idx -= 1

    arr[idx] = switch(arr[idx])

    add = 1
    while idx - add >= 0 and idx + add < length:
        if arr[idx - add] == arr[idx + add]:
            arr[idx - add] = switch(arr[idx - add])
            arr[idx + add] = switch(arr[idx + add])
        else:
            break

        add += 1


for _ in range(k):
    gender, num = map(int, stdin.readline().split())

    if gender == 1:
        boy(num, switches)
    elif gender == 2:
        girl(num, switches)

cnt = 0
for s in switches:
    print(s, end=" ")
    cnt += 1

    if cnt and cnt % 20 == 0:
        print()
