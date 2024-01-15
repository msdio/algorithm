from sys import stdin

'''
n!의 소인수 분해 시 포함된 k의 개수
'''
n, a = map(int, stdin.readline().split())

ans = 0
for i in range(1, n):
    if a**i > n:
        break

    ans += (n // (a**i))

print(ans)
