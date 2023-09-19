from collections import deque


N = int(input())

board = [[0 for i in range(N)] for j in range(N)]

K = int(input())

for _ in range(K) :
    a,b  = list(map(int, input().split()))
    board[a-1][b-1] = 1

L = int(input())

dic = {}
for _ in range(L):
    t, move = list(map(str, input().split()))
    t = int(t)
    dic[t] = move

snake= deque()
# snake = [(0,0)]
snake.append((0,0))


move = (0,1)
moves = [(0,1), (1,0), (0,-1), (-1,0)]
time = 0
while True:
    time += 1


    rx, ry = snake.popleft()
    flag = False
    fx, fy = 0,0
    if len(snake) > 0:
        flag = True
        fx, fy = snake.pop()
    else:
        fx, fy = rx, ry
    dx, dy = move
    x = fx + dx
    y = fy + dy

    if x >= N or y >= N or x < 0 or y <0:
        print(time)
        exit(0)
    snli = list(snake)
    snli.append((rx,ry))
    if (x,y) in list(snli):
        print(time)
        exit(0)

    if flag:
        snake.append((fx, fy))

    if board[x][y] == 1:
        board[x][y] = 0
        snake.appendleft((rx, ry))
        snake.append((x, y))
    else:
        snake.append((x, y))

    


    # print(f"time : snake = {time}, {snake}" )
    
    
    if time in dic:
        if dic[time] == 'D':
            idx = moves.index(move)
            idx += 1
            idx %= 4
            move = moves[idx]
        else:
            idx = moves.index(move)
            idx -= 1
            idx %= 4
            move = moves[idx]

    # for i in range(N) :
    #     for j in range(N):
    #         if (i,j) in snake:
    #             print('#', end = "")
    #         else:
    #             print(board[i][j], end="")
    #     print()