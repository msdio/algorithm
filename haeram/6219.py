from sys import stdin

'''
1. 에라토스테네스의 체로 B까지의 소수를 구한다
2. A~B까지 돌면서 숫자에 D가 포함되어 있는지 확인
  2-1. string으로 변환 후 확인
'''

a, b, d = map(int, stdin.readline().split())

# get prime numbers
primes = [1 for _ in range(b+1)]
primes[1] = 0
for i in range(2, b+1):
    if not primes[i]:
        continue

    for j in range(2*i, b+1, i):
        primes[j] = 0

# main
ans = 0
for i in range(a, b+1):
    if not primes[i]:
        continue

    cand = str(i)

    if str(d) in cand:
        ans += 1


print(ans)
