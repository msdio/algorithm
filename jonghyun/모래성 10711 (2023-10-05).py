from collections import deque

N, M = map(int, input().split())
board = []
check = [[0 for _ in range(M)] for j in range(N)]
moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

for _ in range(N):
    li = list(input())
    for i in range(len(li)):
        if li[i] != '.':
            li[i] = int(li[i])
    board.append(li)
# print(*board, sep = "\n")

dq = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            continue

        

        for dx, dy in moves:
            x = i + dx
            y = j + dy
            if board[x][y] == '.':
                board[i][j] -= 1

        if board[i][j] <= 0:
            dq.append([(i,j), 0])
            check[i][j] = 1
            

answer = -1
while len(dq) != 0:
    coord, depth = dq.popleft()
    i, j= coord

    if depth > answer:
        answer = depth
        # print(f"depth : {depth}")
        # for ii in board:
        #     for jj in ii:
        #         print(jj, end="")
        #     print()
        

    for dx, dy in moves:
        x = i + dx
        y = j + dy
        if check[x][y] == 1:
            continue
        if board[x][y] != '.':
            board[x][y] -= 1
            if board[x][y] <= 0:
                dq.append([(x,y), depth + 1])
                check[x][y] = 1
        
        
                

print(answer +1)