from collections import deque
arrows = [(1,0), (-1,0), (0,1), (0,-1)]
board = []
swan_point = []
melt_dq = deque()



r, c = list(map(int, input().split()))
for i in range(r) :
    li = list(input())
    if 'L' in li :
        swan_point.append((i , li.index('L')))
    board.append(li)


class Main :
    board = []
    swan_check = []
    swan_point = []
    swan1_dq = deque()
    swan2_dq = deque()
    ice1_dq = deque()
    arrows = [(1,0), (-1,0), (0,1), (0,-1)]
    r = 0
    c = 0



main = Main()
main.solution()



'''
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...
'''

