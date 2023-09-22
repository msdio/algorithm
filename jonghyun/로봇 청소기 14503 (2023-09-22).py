
directions = [(-1,0), (0,1), (1,0), (0,-1)]
N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
direction = directions[d]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0

while True:
    if board[r][c] == 0:
        answer += 1
        board[r][c] = 2

    f_flag = True
    for dx, dy in directions:
        x = r + dx
        y = c + dy
        if x >= N or y >= M or x <0 or y <0:
            continue
        if board[x][y] == 0:
            f_flag = False
    
    if f_flag:
        b = (d+2) % 4
        back_direction = directions[b]
        r += back_direction[0]
        c += back_direction[1]
        if board[r][c] == 1:
            print(answer)
            exit(0)
        continue

    
    f_flag = False
    for dx, dy in directions:
        x = r + dx
        y = c + dy
        if x >= N or y >= M or x <0 or y <0:
            continue
        if board[x][y] == 0:
            f_flag = True
    
    if f_flag:
        d = (d+3) % 4
        back_direction = directions[d]
        x = r + back_direction[0]
        y = c + back_direction[1]

        if x >= N or y >= M or x <0 or y <0:
            continue
        if board[x][y] == 0:
            r, c = x, y
