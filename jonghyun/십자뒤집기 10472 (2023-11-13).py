from itertools import permutations, combinations

arr = []

for i in range(10):
    for k in combinations([j for j in range(9)], i):
        arr.append(k)

# print(len(arr))

def change(board, index):
    directions = [(1,0),(-1,0),(0,-1),(0,1),(0,0)]
    coordinate = (index//3, index%3)

    x, y = coordinate
    for dx, dy in directions:
        a, b = x + dx, y + dy
        if a < 0 or a >= 3 or b < 0 or b >= 3:
            continue
        if board[a][b] == '*':
            board[a][b] = '.'
        else:
            board[a][b] = '*'

    


T = int(input())
for i in range(T):
    board = []
    for j in range(3):
        board.append(list(input()))

    

    for pos in arr:
        board_copy = [b[:] for b in board]

        # print( pos)
        for p in pos:
            change(board_copy, p)
        
        # print(*board_copy, sep = "\n")


        flag = True
        for ii in range(3):
            for jj in range(3):
                if board_copy[ii][jj] == '*':
                    flag = False
        if flag:
            print(len(pos))
            break
    

'''
1
*..
**.
*..
'''
    