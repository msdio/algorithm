from sys import stdin

'''
살아있는 신호등은 1, 망가진건 0으로 배열을 하나 만든다음에
K만큼의 길이로 검사하면서 그 안에 0이 몇개 있는지 센다
0을 만나면 바로 return

시간초과 왜 날까?
for문 안에 slicing 하는 부분 때문인 것 같다.

그럼 매번 슬라이싱 하지 않고, start, end 값을 가지고 더하고 빼면서 진행하자

'''

n, k, b = map(int, stdin.readline().split())

arr = [1 for _ in range(n+1)]
for _ in range(b):
    broken = int(stdin.readline())
    arr[broken] = 0


# 초기값을 세팅
window = arr[1:k+1].count(0)
ans = window

for i in range(2, n-k+2):
    if arr[i-1] == 0:
        window -= 1

    if arr[i+k-1] == 0:
        window += 1

    ans = min(ans, window)

print(ans)
