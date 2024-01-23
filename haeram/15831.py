from sys import stdin

'''
B 개수가 넘으면 s 계속 줄이면서 확인

ans 값은 B, W 조건이 맞으면 e - s + 1로 계속 최신화
'''

n, b, w = map(int, stdin.readline().split())
road = stdin.readline()

start, end = 0, 0
b_cnt, w_cnt = 0, 0

ans = 0

while end < n:
    if road[end] == 'B':
        b_cnt += 1
    elif road[end] == 'W':
        w_cnt += 1

    while b_cnt > b:
        if road[start] == 'B':
            b_cnt -= 1
        else:
            w_cnt -= 1

        start += 1

    if b_cnt <= b and w_cnt >= w:
        ans = max(ans, end - start + 1)

    end += 1

print(ans)
