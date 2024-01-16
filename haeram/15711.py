from sys import stdin

'''
1. a+b 가 짝수면 YES
2. a+b 가 홀수라면 a+b-2 가 소수인지 확인
=> 5 * 10^8 로 시간 초과
'''

# t = int(stdin.readline())

# def is_prime(n):
#     for i in range(2, n+1):
#         if i*i > n:
#             break

#         if (n % i == 0):
#             return False

#     return True


# for _ in range(t):
#     a, b = map(int, stdin.readline().split())

#     if ((a+b) % 2 == 0):
#         print('YES')
#         continue

#     if (is_prime(a+b-2)):
#         print('YES')
#     else:
#         print('NO')

#####################################################

'''
최대 길이는 4 * 10^12
이것의 root인 2 * 10^6 까지 소수를 모두 구함

1. a+b 가 짝수면 YES
2. a+b 가 홀수라면 a+b-2 가 소수인지 확인

2 * 10^6 + 500 으로 시간복잡도가 줄음
'''

# t = int(stdin.readline())

# max_len = 2 * 10**6 + 1
# is_prime = [1 for i in range(max_len)]
# is_prime[0] = 0
# is_prime[1] = 0

# # get all prime numbers
# for i in range(2, max_len):
#     if (not is_prime[i]):
#         continue

#     for j in range(2*i, max_len, i):
#         is_prime[j] = 0

# # main
# for _ in range(t):
#     a, b = map(int, stdin.readline().split())

#     if a+b < 4:
#         print('NO')
#     elif (a+b) % 2 == 0:
#         print('YES')
#     else:
#         if (is_prime[a+b-2]):
#             print('YES')
#         else:
#             print('NO')


"""
A+B가 2가 아닌 짝수면 가능하다.

홀수면 무조건 홀수 + 짝수의 형태여야 한다.
따라서 2 + 홀수의 형태가 되어야 하고, 홀수는 소수여야 한다.
즉 홀수인 경우에는 (홀수-2)가 소수인지 확인하면 된다.
"""

t = int(stdin.readline())

lines = []

# 가장 긴 끈의 길이 구하기
max_line = 0
for _ in range(t):
    a, b = map(int, stdin.readline().split())

    max_line = max(max_line, int((a + b) ** 0.5))
    lines.append([a, b])

# 에라토스테네스의 체
arr = [1 for _ in range(max_line + 1)]
arr[0] = 0
arr[1] = 0
for i in range(2, max_line + 1):
    if not arr[i]:
        continue

    for j in range(2 * i, max_line + 1, i):
        arr[j] = 0

# 모든 소수 구하기
primes = [i for i in range(max_line + 1) if arr[i]]


def is_prime(n):
    for prime in primes:
        if prime**2 > n:
            break

        if n % prime == 0:
            return False

    return True


# main
for line in lines:
    a, b = line

    if a + b < 4:
        print("NO")
        continue

    if (a + b) % 2 == 0:
        print("YES")
        continue

    if is_prime(a + b - 2):
        print("YES")
    else:
        print("NO")
