def changeDirection(direction):
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    else:
        return 2

def plusMove(X, x, z, direction):
    # print(f"X,x,z, direction : {X,x,z, direction}")
    if 0 <= z <= (X-x-1):
        return (z+x, direction)
    elif X-x-1 < z <= (X-x-1) + (X-1):
        return (X - (z-(X-x-1)) -1, changeDirection(direction))
    else:
        return (z - (X-x-1) - (X-1), direction)

def minusMove(X, x, z, direction):
    if 0 <= z <= x:
        return (x-z, direction)
    elif x < z <= x + (X-1):
        return (z-x, changeDirection(direction))
    else:
        return (X - (z-x-(X-1)) - 1, direction)



R, C, M = list(map(int, input().split()))

sharks = []
for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    if d in [1,2]:
        sharks.append([r-1, c-1, s % ((R-1)*2), d-1, z])
    else:
        sharks.append([r-1, c-1, s % ((C-1)*2), d-1, z])

# print(f"time 0 : {sharks}")
answer = 0
for time in range(C):

    minDistance = 0xFFFFF
    index = -1
    for i, shark in enumerate(sharks):
        if shark[1] == time and minDistance > shark[0]:
            minDistance = shark[0]
            index = i
    if index != -1:
        answer += sharks[index][4]
        sharks.pop(index)


    for shark in sharks:
        r, c = shark[0], shark[1]
        if shark[3] == 0:
            shark[0], shark[3] = minusMove(R, r, shark[2], shark[3])
        elif shark[3] == 3:
            shark[1], shark[3] = minusMove(C, c, shark[2], shark[3])

        elif shark[3] == 1:
            shark[0], shark[3] = plusMove(R, r, shark[2], shark[3])
        elif shark[3] == 2:
            shark[1], shark[3] = plusMove(C, c, shark[2], shark[3])
    
    dic = {}
    for i, shark in enumerate(sharks):
        r, c = (shark[0], shark[1])
        if (r, c) not in dic:
            dic[(r, c)] = [i]
        else:
            dic[(r, c)].append(i)

    # print(f"dic : {dic}")

    remove_shark_arr = []
    for key in dic:
        if len(dic[key]) >= 2:
            
            max_weight_shark = (-1,-1,-1,-1,-1)
            for i in dic[key]:
                remove_shark_arr.append(sharks[i])
                if sharks[i][4] > max_weight_shark[4]:
                    max_weight_shark = sharks[i]

            remove_shark_arr.remove(max_weight_shark)

    for remove_target in remove_shark_arr:
        sharks.remove(remove_target)
    
    # print(f"dic : {dic}")
    # print(f"time {time+1} : {sharks}")
print(answer)


'''
2 2 1
1 1 999 1 10000


in:
4 2 2
2 2 3 1 1
4 2 3 1 2

out:
2

'''