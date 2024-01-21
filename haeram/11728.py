from sys import stdin

'''
그냥 concat 한다음 정렬하면 2*10 이다.
근데 이걸 풀어보라고 한건 아닐텐데..
'''

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

arr = a + b
arr.sort()

print(*arr)
