

def isOverlap(compare_head1, compare_head2, status1, before_head, current_head, status2, di) :

    x11, y11 = compare_head1
    x12, y12 = compare_head2
    x21, y21 = before_head
    x22, y22 = current_head
    global L
    if x21 < 0:
        x21 = 1
    if x22 < 0:
        x22 = 1
    if y21 < 0:
        y21 = 0
    if y22 <0 :
        y22 = 0
    
    if y21 >= 2*L+1:
        y21 = 2*L+1
    if y22 >= 2*L+1:
        y22 = 2*L+1
    if x21 >= 2*L+1:
        x21 = 2*L+1
    if x22 >= 2*L+1:
        x22 = 2*L+1
    

    if status1 == status2:
        if status1 == '가로' and x11 == x12 == x21 == x22:
            if y21 <= y11 <= y22 :
                # print(1,compare_head1,compare_head2,before_head,current_head)
                # if di == 1:
                return y11 - y21
                # else :
                    # return y22 - y12
            elif y21 <= y12 <= y22:
                # print(2,compare_head1,compare_head2,before_head,current_head)
                # if di == 1:
                return y22 - y12
                # else :
                    # return y11 - y21
        elif status1 == '세로' and y11 == y12 == y21 == y22:
            if x21 <= x11 <= x22 :
                # print(3,compare_head1,compare_head2,before_head,current_head)
                # if di == 1:
                return x11 - x21
                # else :
                    # return x22 - x12
            elif x21 <= x12 <= x22:
                # print(4, compare_head1,compare_head2,before_head,current_head)
                # if di == 1:
                return x22 - x12
                # else:
                    # return x11 - x21
    else:
        if status1 == '가로' and status2 == '세로':
            if x21 <= x11 <= x22 and y11 <= y21 <= y12:
                # print(5,compare_head1,compare_head2,before_head,current_head)
                if di == 1:
                    return x12 - x21
                else:
                    return x22 - x11
        else:
            if y21 <= y11 <= y22 and x11 <= x21 <= x12:
                # print(6,compare_head1,compare_head2,before_head,current_head)
                if di == -1:
                    return y22 - y11
                else:
                    return y12 - y21
                
    
    return False

L = int(input())
N = int(input())

range_arr = []


directions = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0
direction = directions[d]
head = (L,L)


rotations = []
for _ in range(N):
    t_i, dir_i = input().split()
    rotations.append((int(t_i), dir_i))


rotations.append((int(0xFFFFFFFFFFF), 'L'))
answer = 0

for rotation in rotations:
    
    before_head = head[:]
    dx = direction[0]*rotation[0]
    dy = direction[1]*rotation[0]
    head = (head[0] + dx, head[1] + dy)


    val = INF = 0xFFFFFFFFF
    # 1. 겹쳤는지 확인해주기
    # 1-1 . 범위가 넘어간 경우
    if head[0] >= 2*L+1 or head[1] >= 2*L+1 or head[0] < 0 or head[1] < 0:
        plus = 0
        # print("bfh:", before_head)
        if direction == directions[0]:
            plus = 2*L+1 - before_head[1]
        elif direction == directions[1]:
            plus = 2*L+1 - before_head[0]
        elif direction == directions[2]:
            plus = before_head[1] - 0 + 1
        elif direction == directions[3]:
            plus = before_head[0] - 0 + 1
        
        val = min(val, plus)

    # 1-2 . 자기 몸에 부딪친 경우
    for index, rg in enumerate(range_arr):
        if index == len(range_arr) - 1:
            continue

        tmp_li = [before_head, head]
        tmp_li.sort()
        if direction[0] == 0:
            tmp = isOverlap(rg[0], rg[1], rg[2], tmp_li[0], tmp_li[1], '가로', direction[1])        
        else:
            tmp = isOverlap(rg[0], rg[1], rg[2], tmp_li[0], tmp_li[1], '세로', direction[0])
        
        if tmp == False:
            continue
        else:
            val = min(val, tmp)
    if val != INF:
        print(answer + val)
        exit(0)


    # 2. 겹치지 않았다면 범위 추가 (정렬을 해서)
    answer += rotation[0]
    string = None
    if direction[0] == 0:
        string = '가로'
    else:
        string = '세로'

    tmp_li = [before_head, head]
    tmp_li.sort()
    range_arr.append([tmp_li[0], tmp_li[1], string])


    # 3. 회전
    dir_i = rotation[1]
    if dir_i == 'L':
        d = (d + 3) % 4
    else:
        d = (d + 1) % 4

    direction = directions[d]


    # print(answer, range_arr, direction)



'''
8
11
1 L
4 R
1 R
8 L
1 L
8 R
1 R
8 L
1 L
6 L
10 R
40


4
4
1 L
1 L
2 L
1 L
6




100000000
5
100000000 L
100000000 L
200000000 L
199999999 L
199999999 L
899999997


1
6
1 L
1 L
2 L
2 L
2 L
3 L
9




1
0
2




4
6
2 L
1 R
1 R
3 R
2 R
1 L
16


3
1
1 L
5


3
4
2 L
2 L
1 L
5 R
7



3
3
2 L
4 L
4 R
6



4
4
1 L
1 L
2 L
1 L
6



3
3
1 L
1 L
2 L
9



4
5
1 L
1 R
1 R
1 R
10 L
5




8
11
1 L
4 R
1 R
8 L
1 L
8 R
1 R
8 L
1 L
6 L
10 R
40



TestCase #1

3
4
2 L
2 L
1 L
5 R

=> 7

TestCase #2
3
3
2 L
4 L
4 R

=> 6

TestCase #3
3
3
2 R
1 R
10 R

= 9

TestCase #4
3
3
2 R
10 L
4 R

= 6

TestCase #5
3
3
2 L
10 L
4 R

= 6

TestCase #6
3
3
10 L
4 L
4 R

= 4

TestCase #7
3
3
2 L
4 L
4 R

= 6

TestCase #8
3
4
2 L
2 L
1 L
5 R

= 7

TestCase #9
3
4
2 R
2 R
1 R
5 L

= 7

TestCase #10
3
5
2 R
3 L
1 L
2 L
10 L

= 9

TestCase #11
3
5
2 R
3 R
1 R
2 R
10 L

= 9

TestCase #12
3
5
2 R
3 R
1 R
2 L
10 L

= 13

TestCase #13
3
8
3 R
3 R
6 R
6 R
6 R
2 R
10 L
10 R

= 32

TestCase #14
3
4
3 R
3 R
3 R
3 R

= 12

TestCase #15
3
4
3 R
3 R
3 R
2 R

14

TestCase #16
100000000
4
2 L
2 L
1 L
5 R

7

TestCase #17
1
6
1 L
1 L
2 L
2 L
2 L
2 L

9

TestCase #18
3
8
2 L
2 L
3 L
4 L
4 L
5 L
2 L
7 L

23

TestCase #19
3
8
2 L
2 L
3 L
4 L
4 L
10 L
2 L
7 L

21

TestCase #20
8
11
1 L
4 R
1 R
8 L
1 L
8 R
1 R
8 L
1 L
6 L
10 R

40

TestCase #21
3
1
1 L

5

TestCase #22
3
1
1 R
5

TestCase #23
3
2
1 R
1 R

7

TestCase #24
3
2
1 R
1 L
5

TestCase #25
3
1
10 L
4

TestCase #26
3
3
2 L
4 L
4 R

6

TestCase #27
3
3
1 R
1 R
10 L

7 

TestCase #28
3
3
1 R
1 L
10 L

5 

TestCase #29
3
0

4

TestCase #30
3
14
3 L
1 L
3 R
1 R
3 L
1 L
6 L
1 L
5 R
1 R
4 L
3 L
1 L
2 L

22

TestCase #31
3
16
3 L
1 L
3 R
1 R
3 L
1 L
6 L
6 L
1 L
5 R
1 R
5 L
4 L
1 L
3 R
1 R

49

TestCase #32
3
16
3 L
1 L
3 R
1 R
3 L
1 L
6 L
6 L
1 L
5 R
1 R
5 L
4 L
1 L
3 R
2 R

46

TestCase #33
3
17
3 L
1 L
3 R
1 R
3 L
1 L
6 L
6 L
1 L
5 R
1 R
5 L
4 L
1 L
3 R
1 R
3 L

49

TestCase #34
3
1
1 L

5

TestCase #35
1
1
1 L

3

TestCase #36
3
5
3 L
1 L
6 L
1 L
2 L

14

TestCase #37
3
5
3 L
1 L
6 L
1 L
2 R

17

TestCase #37
3
5
3 L
1 L
6 L
1 L
3 R

14

TestCase #37
3
5
3 L
1 L
6 L
1 L
100000 R

14



4
4
1 L
1 L
2 L
1 L



4
5
1 L
1 R
1 R
1 R
10 L



'''