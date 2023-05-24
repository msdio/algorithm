n = 0
switch = []
students = []
student_num = 0

def man(num) :
    global n, switch, student_num

    for i in range(n) :
        if (i + 1) % num == 0 :
            if switch[i] == 1 :
                switch[i] = 0
            else :
                switch[i] = 1

def woman(num) :
    global n, switch, students
    num -= 1
    move = (num , num)
    index = 1
    while True :
        if num - index < 0 or num + index >= n :
            break
        if switch[num - index] == switch[num + index] :
            move = (num - index, num + index)
            index += 1
        else :
            break
    # print(move)
    for i in range(move[0], move[1] + 1) :
        if switch[i] == 1 :
                switch[i] = 0
        else :
            switch[i] = 1

def solution() :
    global n, switch, students, student_num
    n = int(input())
    switch = list(map(int,input().split()))
    student_num = int(input())
    students = []
    for i in range(student_num) :
        students.append(list(map(int,input().split())))
    
    for student in students :
        if student[0] == 1 :
            man(student[1])
        else :
            woman(student[1])
    
    for i in range(n) :
        # print("i", i)
        if (i+1) % 20 == 0 :
            print(switch[i])
            continue
        print(switch[i], end = ' ')
        

solution()


'''
24
0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1
3
1 3
2 3
2 7


1
0 
3
1 1
2 1
2 1
'''