
def backtracking(i,j) :
    global board, n, check, boxes
    # print(board)
    if i >= n :
        
        for bo in board :
            for b in bo :
                print(b[1], end = " ")
            print()
        dic = {}
        for index, box in enumerate(boxes) :
            dic[box[1]] = check[index]
            # print(f"check[{index}] : {check[index]}")
        
        for bo in board :
            for b in bo :
                print((dic[b[1]] + 1) % 4, end = " ")
            print()
        exit(0)
    else :
        # 가능한 경우를 frame에 넣음. -1의 경우는 와일드카드. 어떤 숫자든 가능
        frame = []
        for idx, dk in enumerate([(0,1), (1,0), (0,-1), (-1,0)]) :
            di, dj = dk
            x = i + di
            y = j + dj
            # 범위를 벗어난 경우는 0이 들어가도록
            if x >= n or y >= n or x < 0 or y < 0 :
                frame.append(0)
                continue
            else :
                if len(board[x][y]) == 0 :
                    frame.append(-1)
                else :
                    frame.append(board[x][y][0][(idx + 2) % 4])
        # print(f"frame : {frame}, i,j : {(i, j)}")
        for index, box in enumerate(boxes) :
            # 이미 들른적 있다면 나가리
            if check[index] >= 0 :
                continue
            else :
                li = box[0]
                num = box[1]
                
                # 4번 회전
                for a in range(4) :
                    tmp_li = li[4-a:4] + li[0:4-a]
                    # tmp_li = li[a:4] + li[0:a]


                    flag = True
                    for b in range(4) :
                        if frame[b] == -1 :
                            continue
                        if tmp_li[b] != frame[b] :
                            flag = False
                    
                    # 실제로 저 배열에 들어갈 수 있는 경우
                    if flag :
                        di = i
                        dj = j
                        if dj >= n - 1:
                            dj -= n
                            di += 1
                            dj += 1
                        else :
                            dj += 1
                        # 체크를 회전횟수로!
                        check[index] = a
                        board[i][j] = [tmp_li, num]
                        backtracking(di, dj)
                        board[i][j] = []
                        check[index] = -1


n = int(input())


zero_two_boxes = []
zero_one_boxes = []
boxes = []
for i in range(n**2) :
    num, a,b,c,d = list(map(int,input().split()))
    li = [a,b,c,d]
    zero = 0
    boxes.append((li, num))
# print(boxes)
check = [-1 for j in range(n**2)]
board = [[[] for j in range(n)] for i in range(n)]

backtracking(0,0)


'''

2
2 0 0 3 1
3 0 2 4 0
1 0 1 2 0
4 0 4 3 0

# 1 2 
# 3 4 
# 0 0 
# 3 2 



2
4 0 0 1 2
2 0 3 1 0
3 4 0 0 2
1 0 0 4 3

# 1 3 
# 2 4 
# 3 3 
# 3 1 



3
1 2 0 3 6
2 5 0 0 2
3 0 4 3 0
4 0 8 5 4
5 2 4 0 0
6 5 6 9 6
7 0 0 3 8
8 9 2 0 4
9 3 0 5 6

# 2 8 5 
# 9 6 1 
# 7 4 3 
# 2 2 2 
# 2 2 0 
# 2 2 2



2
2 0 3 1 0
3 4 0 0 2
1 1 2 0 0
4 0 0 4 3
# 2 4
# 1 3
# 3 3
# 3 3

2
2 0 0 3 1
3 0 2 4 0
1 0 1 2 0
4 0 4 3 0
# 2 4
# 1 3
# 2 0
# 2 1
'''