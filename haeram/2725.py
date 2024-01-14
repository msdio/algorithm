# from sys import stdin

# c = int(stdin.readline())

'''
1. 에라토스테네스의 체를 통해 최댓값까지의 소수 계산
2. 1번의 배열을 이용해 N까지의 소수 개수 계산 = k라 가정
  2-1. 배열에 N까지의 소수 개수를 업데이트 해놓기
3. kP2 + 2*k + 1가 정답 
  3-1. 소수인 수 2개 조합하는 경우의 수 kP2
  3-2. x나 y중 하나 좌표가 1인 경우의 수 2*k 개
  3-3. (1, 1)은 중복되므로 -1
  3-4. (0, 1), (1, 0) 두 개는 + 2
4. 이 때 1도 고려해야 하므로 +3을 더해줘야 함

이렇게 풀면 안된다. 기울기로 접근해야 할듯
'''

# arr = [int(stdin.readline()) for _ in range(c)]
# max_num = max(arr)

# # get primes
# primes = [1 for _ in range(max_num + 1)]
# primes[0] = 0
# primes[1] = 0
# for i in range(2, max_num+1):
#     if not primes[i]:
#         continue

#     for j in range(2*i, max_num+1, i):
#         primes[j] = 0

# # count primes until index i
# for i in range(2, max_num+1):
#     primes[i] = primes[i] + primes[i-1]

# # main
# for point in arr:
#     if point == 0:
#         print(0)
#         continue

#     if point == 1:
#         print(3)
#         continue

#     prime_cnt = primes[point]

#     ans = prime_cnt * (prime_cnt-1) + 2 * point + 1
#     print(ans)

'''
기울기가 고유한 애들을 구해야 한다.

분모가 3인 경우 분자는 2
분모가 4인 경우 분자는 3
분모가 5인 경우 분자는 2, 3, 4 가능

분모와 분자가 서로소인 경우를 찾아야 함
서로소는 곧 gcd가 1인 것

위에서 구한 서로소 개수 * 2 하고,
맨 마지막에 (0, 1), (1, 0), (1, 1) 3개 더해야 함

결론적으로 서로소개수*2 + 3이 정답

근데 이렇게 하면 매번 gcd 구하니까 계산도 반복됨
이 전에 구한 개수 + 분모가 n인 경우의 기울기 개수 하면 됨 (dp)
'''

from sys import stdin
c = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(c)]


def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


# main
max_num = max(arr)
dp = [0 for _ in range(max_num+1)]
dp[1] = 3

# 서로소 개수 구하기
for i in range(2, max_num + 1):
    cnt = 0

    for j in range(1, i):
        if (gcd(i, j) == 1):
            cnt += 1

    dp[i] = dp[i-1] + 2*cnt


for point in arr:
    # 서로소 개수 구하기
    print(dp[point])
