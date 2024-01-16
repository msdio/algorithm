from sys import stdin

'''
1. 최소 공약수에서 최소 공배수를 나눈다
2. 이걸 소인수 분해를 하고 얘네를 적절히 나누면 된다
3. 최대한 차이가 덜 나도록 분배하고
4. 분배 된 수 * 최소공배수 하면 답

분배를 어떻게 할 것인가?
lcm/gcd 값 = n이라고 치면
하나씩 나눠보면서 n에 가장 가까워지는 경우를 찾으면 된다.

이러면 소인수 분해는 안해도 된다.
'''

gcd, lcm = map(int, stdin.readline().split())


def is_seoroso(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


# main
target = lcm // gcd

ans = []
for i in range(int(target**0.5), 0, -1):
    if target % i == 0 and is_seoroso(target // i, i) == 1:
        ans.append((target // i) * gcd)
        ans.append(i * gcd)
        break

print(*sorted(ans))
