from sys import stdin

"""
완탐으로 하면
1. 시작점 위치를 고르고 (n)
2. 거기서 간격 1씩 늘려가면서 남은 점들을 다 확인한다 (2억)

이렇게 하면 당연히 안되니 점들을 dictionary로 저장해놓고
현재 점을 i라고 하면 i+2, i+4를 찾는다? 근데 이것도 안되겠다

양 끝 점을 고르고 만약에 사이 길이가 
짝수라면 가운데 점이 있을 수가 없다.
홀수라면 중간 지점에 점이 있나 확인한다.

그러면 점이 n개니까 n^2에 해결된다.
"""

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    x = list(map(int, stdin.readline().split()))
    x.sort()

    dict = {}
    for point in x:
        dict[point] = 1

    ans = 0
    for i in range(n - 2):  # n 뒤에 숫자가 두 개 이하라면 가능한 경우가 없다.
        for j in range(i + 2, n):  # 사이에 최소 숫자 하나는 있어야 하니까 i+2부터 시작
            if (x[j] - x[i] + 1) % 2 == 0:  # 차이가 짝수라면 가능한 경우가 없다.
                continue

            if (x[j] + x[i]) // 2 in dict:
                ans += 1

    print(ans)
