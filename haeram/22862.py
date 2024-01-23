from sys import stdin

"""
홀수 짝수 판별하기 귀찮으니까 
홀 1 짝 0으로 바꾼다. 
그러면 1이 K개 포함되어 있는 배열 중 가장 긴 배열을 찾으면 된다.

그 배열은 또 어떻게 찾을까.
범위의 처음값을 start, 끝 값을 end 라고 하자.
1의 개수가 k보다 작으면 end 값을 계속 키우고,
k보다 커지는 순간 end 값을 줄이고 start 값을 늘린다.

다시 1 개수가 줄어들면 end 값을 올린다.
end가 n보다 커지면 그만한다. 
start를 올리면 값이 작아질 뿐이니까 end가 n보다 큰 순간에 start를 더 볼 필요는 없다.

매번 end - start 값이 길이 값을 저장햇다가 최대값을 구한다.
"""

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for i in range(n):
    if arr[i] % 2 == 0:
        arr[i] = 0
    else:
        arr[i] = 1

start = 0
end = 0

cur_odd = 0
ans = 0

while end < n:
    if arr[end] == 1:
        cur_odd += 1

    # 만약 k보다 홀수 개수가 많아지면 start 증가
    if cur_odd > k:
        ans = max(ans, end - start)
        cur_odd -= 1

        if arr[start] == 1:
            cur_odd -= 1

        start += 1
        continue

    ans = max(ans, end - start)
    end += 1

ans = max(ans, end - start)
print(ans - cur_odd)
