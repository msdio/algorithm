import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

N,M,A,B,K = map(int,input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = -1


sx,sy = map(int,input().split())
ex,ey = map(int,input().split())


def find_something(x,y):
    for i in range(A):
        for j in range(B):
            if board[x+i][y+j] != 0:
                return False
    return True


def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    visited = [[2147000000 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 0

    while dq:
        xx,yy = dq.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<M and 0<=nx+A-1<N and 0<= ny+B-1<M:
                if find_something(nx,ny) == False:
                    continue
                
                if visited[nx][ny] > visited[xx][yy] + 1:
                    visited[nx][ny] = visited[xx][yy] + 1
                    dq.append((nx,ny))
    return (visited[ex-1][ey-1])

print(BFS(sx-1,sy-1) if BFS(sx-1,sy-1) <2147000000 else -1)
    

