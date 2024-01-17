from sys import stdin

"""
1. 홀수는 무조건 1이다.
2. 대충 f(32)까지 구해보면 f(2n) = 2f(n) 규칙이 보인다.
  2-1. 사실 생각해보면 당연한 공식이다. 2를 한번 더 곱한거니까
3. f(1) + f(2) + ... f(n) = s(n)이라고 하자
  그러면 f(a) + f(a + 1) + ... + f(b)는
  s(b) - s(a-1)과 같다.

그러면 s(n)의 규칙을 찾아보자.
4. n이 홀수일 경우, 1번에 의해 s(n-1) + 1 이다.
5. n이 짝수일 경우, s(12)정도까지 구해보면 s(2n) = 2*s(n/2) + n/2 인게 보인다.
6. 홀수인 경우도 s(2n+1) = 2*s(n/2) + n/2 + 1

** 2의 0승도 있으니까 1도 있다. **
"""

a, b = map(int, stdin.readline().split())


def sum_squares(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    if num % 2 == 1:
        return 2 * sum_squares(num // 2) + num // 2 + 1
    elif num % 2 == 0:
        return 2 * sum_squares(num // 2) + num // 2

    return 0


print(sum_squares(b) - sum_squares(a - 1))
