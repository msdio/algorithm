from sys import stdin
import sys

a, b, c, n = map(int, stdin.readline().split())

if (n % a == 0 or n % b == 0 or n % c == 0):
    print(1)
    sys.exit(0)

for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if (a*i + b*j + c*k == n):
                print(1)
                sys.exit(0)

print(0)
