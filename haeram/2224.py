from sys import stdin

x = int(stdin.readline())

arr = [[0] * 58 for _ in range(58)]
cnt = 0

for _ in range(x):
    [prev, next] = stdin.readline().split("=>")
    prev = prev.strip()
    next = next.strip()

    if prev == next:
        continue

    prev_idx = ord(prev) - 65
    next_idx = ord(next) - 65
    if not arr[prev_idx][next_idx]:
        arr[prev_idx][next_idx] = 1
        cnt += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i == j or arr[i][j]:
                continue

            if arr[i][k] and arr[k][j]:  # 연결 관계 적용
                arr[i][j] = 1
                cnt += 1

print(cnt)  # 개수

for i in range(58):
    for j in range(58):
        if arr[i][j]:
            print(f"{chr(i+65)} => {chr(j+65)}")
