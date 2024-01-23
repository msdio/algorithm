from sys import stdin

"""
눈사람의 머리 몸통은 신경쓰지 않고, 2개씩 고르면 된다.
nC2로 먼저 2개 뽑고, n-2C2로 남은 것 중에 2개 고르면 되긴 한다.
그러면 n^4 이니까... 6^4 * 10^8, 절대 안된다.

n^3은 108 * 10^6 = 1.08 * 10^8, 될 것 같다.
그러면 일단 2개 뽑고 나머지 애들은 O(n)으로 할 방법을 궁리해보자.

우선 두 개를 뽑은 것의 합을 구한다.
시작지점을 s, 끝 지점을 e라고 했을 때 
정렬 먼저 하고
s+e값이 합보다 크다면 e를 줄이고, 
작다면 s를 증가시키는 방향으로 이동하면 된다.
"""

n = int(stdin.readline())
snow = list(map(int, stdin.readline().split()))

snow.sort()


# 이미 사용된 눈덩이 두 개를 제외하고, 차이가 최소가 되는
def make_snowman(n, arr, index1, index2):
    height = arr[index1] + arr[index2]
    cur_min = height

    start = 0
    end = n - 1

    while start < end:
        if start == i or start == j:
            start += 1
            continue

        if end == i or end == j:
            end -= 1
            continue

        cur_height = arr[start] + arr[end]
        if cur_height == height:
            return 0

        if cur_height > height:
            end -= 1
        else:  # cur_height < height 인 경우
            start += 1

        cur_min = min(cur_min, abs(height - cur_height))

    return cur_min


# main
ans = 10**9
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = min(ans, make_snowman(n, snow, i, j))

print(ans)
