from sys import stdin

'''
합
n*(n+1)/2 이용하면 됨

GCD
간격이 무조건 d이다. 따라서 약수에 d가 포함되어야 한다.
a만큼 평행이동 한 것이니까... a도 나눠 떨어져야 한다.
그럼 a와 d의 gcd랑 똑같은건가?

그러면 l, r값은 관련이 없는건가

+ l == r인 경우도 고려해야 한다.

합인 경우는 a지만,
gcd인 경우는 수가 하나니까 이건 l과 r이 모두 GCD다.

-> l과 r이 GCD가 아니라... l번째 항이 답이다. 즉 a + d(l-1)
'''

a, d = map(int, stdin.readline().split())
q = int(stdin.readline())


def get_sum(start, end, a, d):
    if start == end:
        return a

    ret = (end - (start-1))*a

    ret += d*((end-1)*end/2 - (start-2)*(start-1)/2)

    return int(ret)


def get_gcd(start, end, a, d):
    if start == end:
        return a + d*(start-1)

    if d == 0:
        return a

    while a % d != 0:
        a, d = d, a % d

    return d


for _ in range(q):
    t, l, r = map(int, stdin.readline().split())

    if t == 1:
        print(get_sum(l, r, a, d))
    else:
        print(get_gcd(l, r, a, d))
