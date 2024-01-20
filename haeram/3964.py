from sys import stdin

'''
n!에서 k의 개수를 세는 것과 같은 문제

k가 있는 경우, k^2이 있는 경우, k^3이 있는 경우, ... 
k<n인 k에 대해서 하면 됨

만약 소수인 경우에는 위처럼 하면 되는데, 
소수가 아니면 
1. 소인수 분해를 한 다음
2. 각 소인수의 지수의 최소값을 구하면 됨

이 때 소인수가 1개씩 있는 경우가 아니라면(12같은 경우),
약수 개수의 배수만큼 처리해줘야 한다.
12의 경우는 2^2 * 3 이니까 2는 2개 단위로 건너뛰어야 함.
'''

t = int(stdin.readline())


def is_prime(n):
    if (n < 2):
        return False

    for i in range(2, n):
        if i*i > n:
            return True

        if n % i == 0:
            return False

    return True


def factorize(n):  # 소인수분해
    ret = []

    temp = n
    for i in range(2, n):
        if i*i > n:
            break

        while temp % i == 0:
            ret.append(i)
            temp = temp // i

    if temp != 1:
        ret.append(temp)

    return ret


# main
for _ in range(t):
    n, k = map(int, stdin.readline().split())

    if (is_prime(k)):
        ans = 0
        for i in range(1, n):
            if k ** i > n:
                break

            ans += (n // k**i)

        print(ans)
    else:
        primes = factorize(k)

        ans = []
        for prime in primes:
            cnt = 0
            for i in range(1, n):
                if prime ** i > n:
                    break

                cnt += (n // prime**i)

            ans.append(cnt)

        print(min(ans))
