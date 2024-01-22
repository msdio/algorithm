from sys import stdin

'''
홀수 짝수 판별하기 귀찮으니까 
홀 1 짝 0으로 바꾼다. 
그러면 1이 K개 포함되어 있는 배열 중 가장 긴 배열을 찾으면 된다.

그 배열은 또 어떻게 찾을까.

'''

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for i in range(n):
    if arr[i] % 2 == 0:
        arr[i] = 0
    else:
        arr[i] = 1

print(arr)
