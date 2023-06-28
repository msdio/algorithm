
n = int(input())
board = [[0 for _ in range(n)] for __ in range(n)]
arrows = [[-1,0],[1,0],[0,-1],[0,1]]
students = []
for i in range(n**2) :
    students.append(list(map(int, input().split())))

for student in students :
    location = (-1, -1)
    max_love = -1
    present_near = -1

    for i in range(n) :
        for j in range(n) :
            love = 0
            near = 0
            if board[i][j] != 0 :
                continue

            
            for i_, j_ in arrows :
                x = i + i_
                y = j + j_
                if x >= n or y >= n or x < 0 or y < 0 :
                    continue
                if board[x][y] in student[1:5] :
                    love += 1
                if board[x][y] == 0 :
                    near += 1
            
            if love > max_love or (love == max_love and present_near < near) :
                max_love = love
                present_near = near
                location = (i, j)
    
    board[location[0]][location[1]] = student[0]

answer = 0

for i in range(n) :
    for j in range(n) :
        love = 0

        temp = board[i][j]
        student = []
        for st in students :
            if temp == st[0] :
                student = st

        for i_, j_ in arrows :
            x = i + i_
            y = j + j_
            if x >= n or y >= n or x < 0 or y < 0 :
                continue


            if board[x][y] in student[1:5] :
                love += 1

        if love == 0 :
            continue
        answer += 10 ** (love-1)
print(answer)
