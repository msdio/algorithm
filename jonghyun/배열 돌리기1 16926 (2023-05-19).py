from collections import deque


board = []


def rotate_board(start_point, n_num, m_num, rotate_num):

    global board
    x = start_point[0]
    y = start_point[1]

    arr = []
    for i in range(n_num):
        arr.append(board[x + i][y])

    for i in range(m_num):
        arr.append(board[x + n_num][y + i])

    for i in range(0, n_num ):
        arr.append(board[x + n_num - i][y + m_num])

    for i in range(0, m_num):
        arr.append(board[x][y + m_num - i])

    dq = deque(arr)

    for i in range(rotate_num) :
        dq.appendleft(dq.pop())


    for i in range(n_num):
        board[x + i][y] = dq.popleft()

    for i in range(m_num):
        board[x + n_num][y + i] = dq.popleft()

    for i in range(0, n_num ):
        board[x + n_num - i][y + m_num] = dq.popleft()

    for i in range(0, m_num):
        board[x][y + m_num - i] = dq.popleft()



def solution():
    global board
    n, m, r = list(map(int, input().split()))

    for i in range(n):
        board.append(list(map(int, input().split())))


    x = 0
    y = 0
    n -= 1
    m -= 1
    while n > 0 and m > 0 :
        rotate_board((x,y), n, m, r)
        n -= 2
        m -= 2
        x += 1
        y += 1

    for i in board :
        for j in i :
            print(j, end=' ')
        print()


solution()

'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''


'''
2 10 2
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
'''