

N, M = list(map(int, input().split()))

arr = []
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cameras = []
answer = 0
for i in range(N):
    for j in range(M):
        if 1<= board[i][j] <= 5:
            cameras.append((i,j))

        if board[i][j] == 0:
            answer += 1

def product(li, index, tmp):
    global arr
    if index >= len(li):
        arr.append(tmp[:])
        return

    for i in range(4):
        tmp.append( (li[index], i) )
        product(li, index+1, tmp)
        tmp.pop()

tmp = []
product(cameras, 0, tmp)

def fillBoard(board, x,dx,y,dy):
    global N, M

    index = 1
    while True:
        i = x + dx*index
        j = y + dy*index
        if i >= N or j >= M or i < 0 or j <0 :
            break
        if board[i][j] == 6:
            break
        board[i][j] = '#'
        index +=1

def fillOne(board, x,y,direction):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    dx, dy = dir[direction]
    fillBoard(board, x,dx,y,dy)

    
def fillTwo(board, x,y,direction):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    dx, dy = dir[direction]
    fillBoard(board, x,dx,y,dy)

    dx, dy = dir[(direction+2) % 4]
    fillBoard(board, x,dx,y,dy)


    
def fillThree(board, x,y,direction):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    dx, dy = dir[direction]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+1) % 4]
    fillBoard(board, x,dx,y,dy)

def fillFour(board, x,y,direction):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    dx, dy = dir[direction]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+1) % 4]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+2) % 4]
    fillBoard(board, x,dx,y,dy) 



def fillFive(board, x,y,direction):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    dx, dy = dir[direction]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+1) % 4]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+2) % 4]
    fillBoard(board, x,dx,y,dy)
    
    dx, dy = dir[(direction+3) % 4]
    fillBoard(board, x,dx,y,dy)    


for info in arr:
    board_copy = [i[:] for i in board]
    for coord, direction in info:
        x, y = coord
        if board[x][y] == 1:
            fillOne(board_copy, x,y, direction)
        if board[x][y] == 2:
            fillTwo(board_copy, x,y, direction)
        if board[x][y] == 3:
            fillThree(board_copy, x,y, direction)
        if board[x][y] == 4:
            fillFour(board_copy, x,y, direction)
        if board[x][y] == 5:
            fillFive(board_copy, x,y, direction)


    size = 0
    for i in board_copy:
        for j in i:
            if j == 0:
                size +=1
    
    def printBoard(board):
        print("====== new Board =====")
        for i in board_copy:
            for j in i:
                print(j,end=" ")
            print()


    # printBoard(board_copy)

    answer = min(answer, size)

print(answer)