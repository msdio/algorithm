from sys import stdin

n, m = map(int, stdin.readline().split())

'''
nCm = n! / { (n-m)! * m! }

2, 5의 제곱 개수 중 작은 것을 구하면 된다.
위 공식을 이용해서 { n!에서의 개수 - (n-r!)에서의 개수 - r에서의 개수 }
로 답을 구한다.
'''


def count_2_and_5(n):
    cnt2, cnt5 = 0, 0

    # count 2
    for i in range(1, n):
        if 2**i > n:
            break

        cnt2 += (n // 2**i)

    # count 5
    for i in range(1, n):
        if 5**i > n:
            break

        cnt5 += (n // 5**i)

    return [cnt2, cnt5]


# main
if m == 0 or n == m:
    print(0)
else:
    ans = min(count_2_and_5(n)) - \
        min(count_2_and_5(n-m)) - min(count_2_and_5(m))

    first = count_2_and_5(n)
    second = count_2_and_5(n-m)
    third = count_2_and_5(m)

    cnt2 = first[0] - second[0] - third[0]
    cnt5 = first[1] - second[1] - third[1]

    print(min(cnt2, cnt5))
