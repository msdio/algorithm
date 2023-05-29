from collections import deque

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

    def __init__(self):
        pass

    def solution(self) :

        self.r, self.c = list(map(int, input().split()))
        for i in range(r) :
            li = list(input())
            if 'L' in li :
                self.swan_point.append((i , li.index('L')))
            self.board.append(li)

        self.init_check()

    def init_check(self) :
        self.swan1_dq.append(self.swan_point[0])
        self.swan2_dq.append(self.swan_point[1])
        self.swan_move(self.swan1_dq)
        self.swan_move(self.swan2_dq)
    
    def swan_move(self, dq):

        self.ice_destroy()

        temp_dq = deque()
        while len(dq) != 0 :
            pop_x, pop_y = dq.popleft()
            for i, j in self.arrows :
                x = i + pop_x 
                y = j + pop_y
                if x >= self.c or y >= self.c or x < 0 or y < 0 :
                    continue
                if self.board[x][y] == '.' and self.check[x][y] == 0 :
                    self.swan_check[x][y] = 1
                    dq.append((x, y))
                if self.board[x][y] == 'X' and self.check[x][y] == 0 :


    def ice_destroy(self):
        pass


main = Main()
main.solution()



'''
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...
'''

