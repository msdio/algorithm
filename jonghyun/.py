N, M = list(map(int, input().split()))
N += 2
M += 2
K = int(input())
board = [[0 for j in range(N)] for i in range(M)]
board_check = [[0 for j in range(N)] for i in range(M)]

for _ in range(K):
    a, b, c, d = list(map(int, input().split()))
    arr = sorted([(a, b), (c, d)]) 
    # arr = [(a, b), (c, d)]
    # arr.sort()


    if c - a == 0 and board_check[arr[1][0] + 1][arr[1][1] + 1] == 2:
        # 가로의 경우
        board_check[arr[1][0] + 1][arr[1][1] + 1] = 3
        continue
    if d - b == 0 and board_check[arr[1][0] + 1][arr[1][1] + 1] == 1:
        # 세로의 경우
        board_check[arr[1][0] + 1][arr[1][1] + 1] = 3
        continue


    if c - a == 0 and board_check[arr[1][0] + 1][arr[1][1] + 1] != 1:
        # 가로의 경우
        board_check[arr[1][0] + 1][arr[1][1] + 1] = 1
        continue
    elif d - b == 0 and board_check[arr[1][0] + 1][arr[1][1] + 1] != 2:
        # 세로의 경우
        board_check[arr[1][0] + 1][arr[1][1] + 1] = 2
        continue



for i in range(1, M):
    for j in range(1, N):
        if i == 1 and j == 1:
            board[i][j] = 1
            continue
        if board_check[i][j] == 1:
            board[i][j] = board[i - 1][j]
        elif board_check[i][j] == 2:
            board[i][j] = board[i][j - 1]
        elif board_check[i][j] >= 3:
            board[i][j] = 0
        else:
            board[i][j] = board[i][j - 1] + board[i - 1][j]
print(board[M-1][N-1])

'''
2 2
2
1 1 2 1
0 2 1 2
'''