from sys import stdin

"""
r, c가 1000개씩이니까 그냥 다 돌면
1000^3 으로 시간안에 불가능하다.

열을 순회하면서 중복인지 확인하는건 줄일 수 없다.
그러니 행을 순회하는 횟수를 줄이면 되지 않을까

만약에 특정 행으로 잘랐는데 중복이 발생하면
그거보다 더 짧은 문자열을 쓰면 무조건 중복이 생기는거다.

그럼 현재 행 높이에서 중복이 생기면 자르는 행 크기를 줄이고
아니면 행 크기를 늘여서 문자열 길이를 늘이면 된다.
"""

r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]


def has_duplicate(row):
    s = set()

    for i in range(c):
        cand = ""
        for j in range(row, r):
            cand += arr[j][i]

        if cand in s:
            return True

        s.add(cand)

    return False


start = 0
end = r - 1
while start <= end:
    mid = (start + end) // 2

    if has_duplicate(mid):  # 중복이 있다면 범위를 늘인다 == 행 크기를 줄인다
        end = mid - 1
    else:
        start = mid + 1

print(end)
