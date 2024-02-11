from sys import stdin

'''
모든 똑같은 수로 나눠야 하니까 먼저 떠오르는게 약수다.

1. 약수로 나눌 수 있는가?
2. 된다면 그 수를 만들기 위해 합치면 된다.

근데 합치는 횟수가 최소가 되려면 약수 중 최소값을 찾으면 된다.

그러면 최소는 배열의 최대값
최대는 배열의 총 합이니까
그 안에서 for문 돌면서

약수일 때 합칠 수 있는지를 확인하면 된다.

합칠 수 있는지는 어떻게 확인하냐

그냥 앞에서부터 더하면 되는거 아닌가?
'''


def can_mod(arr, target):  # 해당 수로 modificate할 수 있는지 확인
    cur_sum = 0
    cnt = 0
    for a in arr:
        if cur_sum > target:
            return False, 0

        cur_sum += a
        if cur_sum == target:
            cur_sum = 0
            continue

        cnt += 1

    return True, cnt


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    start = max(arr)
    end = sum(arr)

    if end == 0:
        print(0)
        continue

    ans = 0
    for i in range(start, end+1):
        if end % i != 0:
            continue

        can, count = can_mod(arr, i)
        if can:
            ans = count
            break

    print(ans)
