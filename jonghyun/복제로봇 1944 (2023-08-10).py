from collections import deque
from heapq import heappop, heappush
N, M = map(int, input().split())

board = []
for _ in range(N) :
    board.append(list(input()))

start = ()
key_list = []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 'S' or board[i][j] == 'K':
            key_list.append((i,j))
            
graph = [[] for _ in range(len(key_list))]
# print(key_list)

for index, key in enumerate(key_list):
    dq = deque()
    dq.append((key, 0))
    check = [[0 for i in range(N)] for j in range(N)]
    check[key[0]][key[1]] = 1
    while len(dq) != 0:
        pop, depth = dq.popleft()
        x, y = pop
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            i = x + dx 
            j = y + dy
            if i >= N or j >= N or i < 0 or j < 0:
                continue
            if board[i][j] == '1':
                continue
            if check[i][j] == 1:
                continue
            if board[i][j] == 'K' or board[i][j] == 'S':
                graph[index].append((key_list.index((i,j)), depth+1))
            dq.append(((i,j), depth+1))
            check[i][j] = 1

pq = []
# print(graph)
tmp = []
for index, val in enumerate(graph):
    for value in val:
        temp = ()
        if index >= value[0] :
            temp = (value[0], index)
        else :
            temp = (index, value[0])
        tmp.append((value[1], temp))

tmp = list(set(tmp))
for i in tmp:
    heappush(pq, i)

answer = 0

def find(x) :
    global parent
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    global parent
    i = find(x)
    j = find(y)
    if i == j :
        return False
    else :
        parent[i] = j
        return True

parent = [i for i in range(len(key_list))]

size = 0
while len(pq) != 0 :
    pop = heappop(pq)
    if union(pop[1][0], pop[1][1]):
        size += 1
        answer += pop[0]
# print(parent)

if size == (len(key_list) -1):
    print(answer)
else :
    print(-1)
'''
5 9
S0K0K
00000
K0K0K
00000
K0K0K
# 16
'''