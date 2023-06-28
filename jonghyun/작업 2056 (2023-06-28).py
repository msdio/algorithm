N = int(input())

task_time = [0] * (N+1)
for i in range(1, N + 1) :
    li = list(map(int, input().split()))

    time = li[0]
    before_task = li[1]
    tasks = li[2:]
    

    if before_task == 0 :
        task_time[i] = time

    temp = 0
    for task in tasks :
        # temp = max(task_time[task][0], temp)
        temp = max(task_time[task], temp)
    # task_time[i] = (temp + time, temp)
    task_time[i] = temp + time

print(max(task_time))