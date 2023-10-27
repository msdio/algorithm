N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key= lambda x : (x[1], x[0]) )

start_time = 0
accumlate_time = 0
for index, value in enumerate(arr):
    ti, si = value

    # print("start_time, accumlate_time :", start_time, accumlate_time)
    if index == 0:
        start_time = si - ti
        accumlate_time = si

        if start_time < 0:
            print(-1)
            exit(0)
        continue
    
    accumlate_time += ti
    if accumlate_time >= si:
        start_time -= accumlate_time - si 
        accumlate_time = si
    
    if start_time < 0:
        print(-1)
        exit(0)

print(start_time)


'''
4
3 5
10 14
5 20
1 16
0


2
4000 40000
25000 30000
'''