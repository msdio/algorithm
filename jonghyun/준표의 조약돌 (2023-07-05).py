N, B, W = list(map(int, input().split()))
roads = input()


i = 0
j = 0
b_present = 0
w_present = 0
answer = 0
if roads[0] == 'W' :
    w_present += 1
else : 
    b_present += 1

if b_present <= B and w_present >= W :
    answer = 1

while j < len(roads):
    j += 1
    if j >= len(roads) :
        break
    
    if roads[j] == 'W':
        w_present += 1
    else :
        b_present += 1

    while b_present > B :
        if roads[i] == 'W' :
            w_present -= 1
        else :
            b_present -= 1
        i += 1
    # print("i, j : ", (i, j) )

    if w_present >= W :
        answer = max( (j - i) + 1, answer)


print(answer)

'''
7 1 1
WBBBBBB
# 7

10 1 2
WBBWWBWWBW
# 5

1 1 1
W
# 1

2 2 0
BB
# 1

1 1 0
B
# 1

2 1 1
WB
# 2

2 1 2
WB
# 0

10 1 0
BBBBBBBBBB
# 1
'''