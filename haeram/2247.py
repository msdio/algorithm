# from sys import stdin
# import sys

# divisor = 10**6

# n = int(stdin.readline())


# def sod(n):  # 약수의 합
#     ret = 0

#     for i in range(2, n):
#         if i*i > n:
#             break

#         if n % i == 0:
#             ret += i

#             if i * i != n:
#                 ret   += (n//i)

#     return ret % divisor


# # main
# ans = 0
# for i in range(2, n+1):
#     ans += (sod(i) % divisor)

# print(ans % divisor)

'''
이렇게 하면 시간복잡도가 NlogN, 풀이 불가능
'''

################################################

'''
2, 3, ..., n까지의 수 중에서
2가 약수인 애들 == 2로 나누어 떨어지는 애들 == n//2 개
3이 약수인 애들 == 3로 나누어 떨어지는 애들 == n//3 개
4이 약수인 애들 == 4로 나누어 떨어지는 애들 == n//4 개
...
k이 약수인 애들 == k로 나누어 떨어지는 애들 == n//k 개

이 때 n // 2 위로는 검사할 필요가 없다. 
왜냐하면 100일 때 51이 약수인 애들은 하나씩밖에 없을것이기 때문.

근데 실질적 약수이므로 자기 자신은 빼야 하니까,
마지막에 한번 씩 더 더해진 2 + 3 + ... + n//2 를 빼면 된다.

따라서 답은 { 2*(n//2) + 3*(n//3) + ... k*(n//k) + ... + n*(n//n) } - sum(2 ~ n//2)
'''

from sys import stdin
import sys
divisor = 10**6

n = int(stdin.readline())

if (n == 1):
    print(0)
    sys.exit(0)


ans = 0
for i in range(2, n // 2 + 1):
    ans += (i*(n//i) % divisor)

half = n // 2
ans -= int(half*(half+1) / 2) % divisor - 1

print(ans % divisor)
