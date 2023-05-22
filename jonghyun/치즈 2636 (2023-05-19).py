from collections import deque

n,m =0,0
board = []
arrow = [(-1,0),(1,0),(0,-1),(0,1)]

def solution() :
    global n,m, board
    n, m = list(map(int, input().split()))
    for i in range(n) :
        board.append(list(map(int, input().split())))

    time = 0
    before_cheese_num = 0
    while True :
        dfs_num = first_dfs(time)
        if dfs_num is False :
            break
        else :
            before_cheese_num = dfs_num
        time += 1

    print(time)
    print(before_cheese_num)


def first_dfs(time):
    global n,m, board


    cheese_num = 0
    cheese_arr = []

    check = [[0 for j in range(m)] for i in range(n)]
    dq = deque()
    dq.append((0, 0))
    check[0][0] = 1
    while len(dq) != 0:
        popleft = dq.popleft()
        pop_x = popleft[0]
        pop_y = popleft[1]
        for direction in arrow :
            x = direction[0] + pop_x
            y = direction[1] + pop_y
            if x >= n or y >= m or x < 0 or y < 0 :
                continue
            if check[x][y] :
                continue
            check[x][y] = 1
            if board[x][y] == 1 :
                cheese_num += 1
                cheese_arr.append((x,y))
                continue
            dq.append((x,y))

    for x, y in cheese_arr :
        board[x][y] = 0

    if cheese_num == 0 :
        return False
    return cheese_num


solution()


'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''