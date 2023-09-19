from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
v = int(stdin.readline())

print(arr.count(v))
