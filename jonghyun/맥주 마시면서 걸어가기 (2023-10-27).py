from collections import deque
t = int(input())

for _ in range(t):
    flag = False
    n = int(input())

    arr = []
    arr.append(list(map(int, input().split())))
    for __ in range(n):
        arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    graph = [[] for _ in range(n+2)]
    check = [0 for _ in range(n+2)]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            distance = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])
            if distance <= 1000:
                graph[i].append(j)
                graph[j].append(i)
    
    dq = deque()
    dq.append(0)
    check[0] = 1
    last = n+1
    flag = False
    
    # print(graph)
    while dq:
        pop = dq.popleft()
        if pop == last:
            flag = True
        for node in graph[pop]:
            if check[node] == 1:
                continue
            check[node] = 1
            dq.append(node)

    if flag:
        print("happy")
    else:
        print("sad")

'''
1
0
0 0
1000 0


1
2
0 0
1000 5
2000 10
3000 15
sad
'''