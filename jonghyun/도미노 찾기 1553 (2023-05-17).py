board = []
board_case = [[] for _ in range(8)]

dice = [[(i,j), (j,i) ]for i in range(7) for j in range(i, 7)]



def dfs(depth, check) :
    global board, board_case, dice
    answer = 0
    if depth == 28 :
        return 1

    for i in range(8):
        for j in range(7):
            if check[i][j] == 1 :
                continue
            if j+1 < 7 and check[i][j+1] != 1 :
                # 가로만
                if board_case[i][j][0] in dice[depth]:
                    check[i][j] = 1
                    check[i][j+1] = 1
                    answer += dfs(depth+1, check)
                    check[i][j] = 0
                    check[i][j + 1] = 0

            if i+1 < 8 and check[i+1][j] != 1:
                # 세로만
                if board_case[i][j][1] in dice[depth]:
                    check[i][j] = 1
                    check[i+1][j] = 1
                    answer += dfs(depth+1, check)
                    check[i][j] = 0
                    check[i + 1][j] = 0
    return answer



def init() :
    global board, board_case, dice

    # print(dice)
    for i in range(8):
        board.append(list(map(int, input())))

    # print(board)
    for i in range(8) :
        for j in range(7) :
            temp = []

            if j + 1 < 7 :
                temp.append((board[i][j], board[i][j+1]))
            else :
                temp.append((-1,-1))

            if i + 1 < 8 :
                temp.append((board[i][j], board[i+1][j]))
            else :
                temp.append((-1,-1))

            board_case[i].append(temp)

    print(dfs(0, [[0 for _ in range(7)] for _ in range(8)]))

    # print(board_case)

'''
0000000
0123456
1111112
1234562
2222333
3456345
3444556
6456566
'''

init()
