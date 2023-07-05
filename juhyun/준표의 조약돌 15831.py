import sys

input = sys.stdin.readline

N,B,W = map(int,input().split())
arr = input().rstrip()
# 30
# 슬라이싱 윈도우? 
lt = 0
rt = 0

black_cnt = 0 # 최대 ~ 까지
white_cnt = 0 # 최소 ~ 부터

cnt = 0
if arr[lt] == 'B':
    black_cnt += 1
elif arr[lt] == 'W':
    white_cnt += 1
    if white_cnt >= W and black_cnt <= B:
        cnt = 1

while lt <= rt <N-1:
    if black_cnt > B: # 검정돌 최대 개수를 넘으면
        if arr[lt] == 'B':
            black_cnt -=1
        elif arr[lt] == 'W':
            white_cnt -=1
        lt += 1
    rt += 1
    if arr[rt] == 'B':
        black_cnt += 1
    elif arr[rt] == 'W':
        white_cnt += 1
    if white_cnt >= W and black_cnt <=B:
        cnt = max(cnt, rt - lt + 1)
print(cnt)

# 2N
        

# 7 2 4
# WWWWWWW
# 7 ok

# 1 1 1
# W
# 1 ok

# 2 1 0
# WB
# 2 ok

# 2 1 0
# BW
# 2 ok

# 1 0 1
# B
# 0

# 2 0 1
# BW
# 1

# 5 2 3
# BWWWB 
# 5

# 6 2 3
# WBBWWB
# 5

# 6 2 1
# WBBBWWB
# 4

# 2 0 1
# BW

