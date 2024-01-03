T = int(input())


directions = [(1,0),(-1,0),(0,1),(0,-1)]


for _ in range(T):
    board = []

    m = 5
    n = 9
    for i in range(m):
        board.append(list(input()))
    
    if _ != T-1:
        input()
    

    pins = []

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'o':
                pins.append((i,j))

    answer = (0xFFFF, 0xFFFF)
    

    def dfs(depth, pins):
        
        global board, answer 
        # print(*board, sep = "\n")
        # print()
        for pin_x, pin_y in pins:
            for dx, dy in directions:
                x = pin_x + dx
                y = pin_y + dy
                xd = pin_x + dx*2
                yd = pin_y + dy*2

                if x >= m or y >= n or x < 0 or y < 0:
                    continue
                if xd >= m or yd >= n or xd < 0 or yd < 0:
                    continue
                if board[x][y] == '#':
                    continue
                if board[x][y] == '.':
                    continue
                if board[xd][yd] != '.':
                    continue
                
                pins_copy= [pin[:] for pin in pins]
                
                if board[x][y] == 'o':

                    pins_copy.remove((pin_x, pin_y))
                    board[pin_x][pin_y] = '.'
                    pins_copy.remove((x, y))
                    board[x][y] = '.'
                    pins_copy.append((xd, yd))
                    board[xd][yd] = 'o'

                    dfs(depth + 1, pins_copy)

                    board[xd][yd] = '.'
                    board[pin_x][pin_y] = 'o'
                    board[x][y] = 'o'

        if answer[0] > len(pins):
            answer = (len(pins), depth)
        elif answer[0] == len(pins):
            answer = (len(pins), min(depth, answer[1]))

    dfs(0, pins)
    print(*answer)
    



'''
1
###...###
..oo.....
......oo.
.........
###...###


1
###...###
.o.......
......o..
...o.....
###o..###

1
###...###
..o......
.....oo..
...o.....
###o..###

1
###...###
..o......
....#oo#.
...o.....
###o..###

1
.........
..oooo...
..oooo...
.........
.........

1
.........
..oooo...
..oo.o...
.........
.........

1
.........
.........
.........
.........
.........

1
.........
...oo....
.........
.........
.........

1
.........
...ooo...
.........
.........
.........

1
oo.oo....
.........
.........
.........
.........

1
oo#......
o........
#........
.........
.........

1
o........
.........
.........
.........
.........


3
#########
##oo#####
#####oo##
#########
#########

#########
##oo#o###
###o#oo##
###oo####
#########

###o#####
#o#oo####
o#o######
o.#o#####
#########

'''