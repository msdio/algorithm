from itertools import combinations
from collections import deque

def killing(archers, board) :
    global D, N, M
    kill = 0

    for time in range(N) :
        arr = []
        for archer in archers :
            
            flag = 0
            dq = deque()
            dq.append([(N-1, archer), 1])
            check = [[0 for i in range(M)] for j in range(N)]
            
            if board[N-1][archer] == 1 :
                arr.append((N-1,archer))
                continue
            while len(dq) != 0 :
                pop = dq.popleft()
                x, y = pop[0]
                distance = pop[1]
                if distance >= D :
                    break
                for dx, dy in [(0,-1),(-1,0),(0,1)]:
                    i = x + dx
                    j = y + dy
                    if i >= N or i < 0 or j >= M or j < 0 :
                        continue
                    if check[i][j] == 1 :
                        continue
                    if board[i][j] == 1 :
                        # board[i][j] = 0
                        arr.append((i,j))
                        flag = 1
                        break
                    check[i][j] = 1
                    dq.append([(i,j), distance + 1])
                if flag == 1 :
                    break
        
        
        arr = list(set(arr))
        # print(kill ,arr, len(arr))
        kill += len(arr)
        for a,b in arr :
            board[a][b] = 0
        
        board.insert(0, [0 for _ in range(M)])
        board.pop(len(board) - 1)
    
    
    return kill


N, M, D = map(int, input().split())
# 세로 길이, 가로 길이
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

# print(board)

temp = [i for i in range(M)]
kill = 0
for i in combinations(temp, 3) :
    board_copy = [b[:] for b in board]
    kill = max(kill, killing(i, board_copy))
print(kill)