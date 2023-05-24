from collections import deque


arrows = [(-1,0),(1,0),(0,1),(0,-1)]

def solution() :
    m, n, a, b, k = list(map(int, input().split()))


    board = [[0] * n for _ in range(m)]
    check = [[0] * n for _ in range(m)]


    
    for i in range(k) :
        x, y = list(map(int, input().split()))
        board[x-1][y-1] = 1

    # print_board(board)
    
    start_point = list(map(int, input().split()))
    start_point[0] -= 1
    start_point[1] -= 1
    end_point = list(map(int, input().split()))
    end_point[0] -= 1
    end_point[1] -= 1
    # print("start end", start_point, end_point)
    # print_board(board)
    
    dq = deque()
    dq.append((start_point,0))
    check[start_point[0]][start_point[1]] = 1

    
    flag = False
    for i in range(a) :
        for j in range(b) :
            x_real_move = start_point[0] + j
            y_real_move = start_point[1] + i

            if x_real_move >= m or x_real_move < 0 :
                flag = True
                break
            if y_real_move >= n or y_real_move < 0 :
                flag = True
                break
            if board[x_real_move][y_real_move] == 1 :
                flag = True
                break
        if flag :
            break
    if flag :
        print(-1)
        return

    if start_point == end_point :
        print(0)
        return


    while len(dq) > 0 :
        pop = dq.popleft()
        pop_x, pop_y = pop[0]
        level = pop[1]
        
        for x, y in arrows :
            x_move = x + pop_x
            y_move = y + pop_y

            flag = False


            if x_move >= m or x_move < 0 or y_move >= n or y_move < 0 :
                continue

            if check[x_move][y_move] == 1 :
                continue

            for i in range(a) :
                for j in range(b) :
                    x_real_move = x_move + j
                    y_real_move = y_move + i

                    if x_real_move >= m or x_real_move < 0 :
                        flag = True
                        break
                    if y_real_move >= n or y_real_move < 0 :
                        flag = True
                        break
                    if board[x_real_move][y_real_move] == 1 :
                        flag = True
                        break
                if flag :
                    break
            if flag :
                continue
            
            
            # print((x_move, y_move))
            if x_move == end_point[0] and y_move == end_point[1] :
                print(level + 1)
                exit(0)
                

            check[x_move][y_move] = 1
            dq.append(((x_move, y_move), level + 1))
    print(-1)
                



def print_board(b) :
    for a in b :
        print(a)


solution()



'''
5 5 2 2 3
2 2
3 2
3 3
4 1
1 4

# 6

5 8 2 2 5
1 6
2 6
3 6
4 3
3 3
4 1
1 7

# 15

5 8 2 2 0
4 1
1 7

# 9

1 1 1 1 0
1 1 
1 1

# 0

5 5 2 2 4
2 2
3 2
3 3
4 1
4 1
1 4

# -1 

2 2 1 1 0
1 1
2 2

# 2


500 500 1 1 1
499 499
1 1
499 499

# -1


5 5 4 4 0
2 1
1 2

# 2

5 5 4 4 0
2 1
1 4

# -1

5 5 1 1 0
1 1
5 5

# 8

5 5 1 1 8
1 2
2 2
3 2
4 2
2 4
3 4
4 4
5 4
1 1
5 5

# 16

5 5 1 1 7
1 2
3 2
4 2
2 4
3 4
4 4
5 4
1 1
5 5

# 10


5 5 1 1 6
1 2
3 2
4 2
2 4
3 4
4 4
1 1
5 5

# 8


5 5 1 1 3
5 4
4 4
4 5
1 1
5 5

# -1


5 5 1 1 3
5 4
4 4
4 5
1 1
4 4

# -1

5 5 2 2 3
5 4
4 4
4 5
1 1
3 3

# -1

5 5 5 5 0
1 1
1 1

# 0 

5 5 5 5 1
5 5
1 1
1 1

# -1
'''