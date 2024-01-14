from sys import stdin
import sys

n = int(stdin.readline())

mapper = {
    '0': '0',
    '1': '1',
    '2': '2',
    '5': '5',
    '6': '9',
    '8': '8',
    '9': '6',
}


def reverse_n(n):
    ret = ''

    for c in str(n):
        if c in ['3', '4', '7']:
            return -1

        ret += mapper[c]

    return int(ret[::-1])


def is_prime(n):
    for i in range(2, n):
        if i*i > n:
            return True

        if n % i == 0:
            return False

    return True


rn = reverse_n(n)

if (rn == -1 or n == 1):
    print('no')
    sys.exit(0)

if (is_prime(n) and is_prime(rn)):
    print('yes')
else:
    print('no')
