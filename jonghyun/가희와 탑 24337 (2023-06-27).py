N, a, b = list(map(int,input().split()))

arr = []

if a >= b :
    for i in range(1, a + 1) :
        arr.append(i)
    temp = []
    for i in range(b - 1, 0, -1) :
        temp.append(i)
    arr.extend(temp)
else :
    for i in range(1, a) :
        arr.append(i)
    temp = []
    for i in range(b , 0, -1) :
        temp.append(i)
    arr.extend(temp)

if len(arr) > N :
    print(-1)
    exit(0)

index = 0
num = N - len(arr)
for i, value in enumerate(arr) :
    if i == 0 :
        continue
    else :
        if arr[i-1] >= 1  and arr[i] >= 1 :
            li1 = arr[:i]
            li2 = [1] * num
            li3 = arr[i:]
            print(*li1, *li2, *li3)
            exit(0)


if a == b == 1 :
    print(*[1]*N)
    exit(0)

print(*arr)


'''
4 3 1
# 1 1 2 3

4 1 3
# 3 2 1 1

5 3 2
# 1 1 2 3 1

5 2 3
# 1 3 2 1 1
-> 1 1 3 2 1

5 3 3
# 1 2 3 2 1
-> 

3 3 1

###### 

5 2 3
#1 1 3 2 1

10 1 9
#9 1 8 7 6 5 4 3 2 
'''