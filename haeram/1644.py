from sys import stdin
import sys

'''
1. 에라토스테네스의 체를 이용해 소수를 n까지 다 구한다.
2. 투 포인터를 이용해 합이 n이 되는 경우를 count한다.
'''

n = int(stdin.readline())

# 에라토스테네스의 체
era = [1 for _ in range(n+1)]
era[0] = 0
era[1] = 0

for i in range(2, n+1):
    if not era[i]:
        continue

    for j in range(i*i, n+1, i):
        era[j] = 0


# get primes
primes = []
for i in range(2, n+1):
    if era[i]:
        primes.append(i)


start = 0
end = 1

ans = 0
if not len(primes):
    print(0)
    sys.exit(0)

cur_sum = primes[0]
if primes.count(n):
    ans += 1

while start < end and end < len(primes):
    if cur_sum == n:
        ans += 1
        cur_sum -= primes[start]
        cur_sum += primes[end]
        start += 1
        end += 1

    if cur_sum < n:
        cur_sum += primes[end]
        end += 1

    if cur_sum > n:
        cur_sum -= primes[start]
        start += 1

print(ans)
