from collections import deque

m, n = map(int,input().split())

board = []
for _ in range(m):
    board.append(list(input()))

R = ()
B = ()
O = ()
for i in range(m):
    for j in range(n):
        if board[i][j] == 'R':
            R = (i,j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            B = (i,j)
            board[i][j] = '.'
        elif board[i][j] == 'O':
            O = (i,j)

dp = [[R,B]]
dq = deque()
dq.append([R, B, 0])
moves = [(1,0), (-1,0), (0,1), (0,-1)]

while len(dq) != 0:
    R, B, depth = dq.popleft()
    rx, ry = R
    bx, by = B
    board[rx][ry] = 'R'
    board[bx][by] = 'B'

    if depth >= 10:
        print(-1)
        exit(0)

    for move in moves:
        dx, dy = move
        b_flag, r_flag = False, False
        b_conflict_flag, r_conflict_flag = False, False
        

        idx = 0
        after_rx, after_ry = rx, ry
        while True:
            
            idx += 1
            temp_rx, temp_ry = rx + dx*idx, ry + dy*idx
            # print(f"temp_rx, temp_ry : {(temp_rx, temp_ry)}, dx, dy : {(dx, dy)}, rx, ry = {(rx, ry)}")
            if temp_rx >= m or temp_ry >= n or temp_rx <0 or temp_ry <0:
                break
            
            if board[temp_rx][temp_ry] == 'O':
                r_flag = True
                break
            if board[temp_rx][temp_ry] == '#':
                break
            if board[temp_rx][temp_ry] == 'B':
                r_conflict_flag = True

            after_rx, after_ry = temp_rx, temp_ry

        idx = 0
        after_bx, after_by = bx, by
        while True:
            idx += 1
            temp_bx, temp_by = bx + dx*idx, by + dy*idx
            if temp_bx >= m or temp_by >= n or temp_bx <0 or temp_by <0:
                break
            if board[temp_bx][temp_by] == 'O':
                b_flag = True
                break
            if board[temp_bx][temp_by] == '#':
                break
            if board[temp_bx][temp_by] == 'R':
                b_conflict_flag = True

            after_bx, after_by = temp_bx, temp_by

        if r_conflict_flag:
            after_rx, after_ry = after_bx - dx, after_by - dy
        if b_conflict_flag:
            after_bx, after_by = after_rx - dx, after_ry - dy

        if r_flag and not(b_flag):
            print(depth + 1)
            exit(0)
        if b_flag:
            continue
        if [(after_rx, after_ry), (after_bx, after_by)] in dp:
            continue
        dp.append([(after_rx, after_ry), (after_bx, after_by)])

        dq.append([(after_rx, after_ry), (after_bx, after_by), depth + 1])

        # print((after_rx, after_ry), (after_bx, after_by))


        # print(f"\n\ndepth = {depth}")
        # for i in range(m):
        #     for j in range(n):
        #         if (i,j) == (after_rx, after_ry):
        #             print("R", end = "")
        #         elif (i,j) == (after_bx, after_by):
        #             print("B", end= "")
        #         else:
        #             print(board[i][j], end="")
        #     print()
    board[rx][ry] = '.'
    board[bx][by] = '.'


print(-1)