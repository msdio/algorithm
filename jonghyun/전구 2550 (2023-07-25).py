from heapq import heappush, heappop

N = int(input())


li1 = list(map(int, input().split()))
li2 = map(int, input().split())

heap = []
graph = [[] for _ in range(N+1)]
dic = {}
for index, value in enumerate(li2) :
    dic[value] = index
    
for index, value in enumerate(li1) :
    n = 0
    size = dic[value]
    # print(f"index, size, value : {index, size, value}")
    for j in range(index+1, N) :
        target = li1[j]
        # print(f"target : {target}")
        if dic[target] <= size :
            graph[value].append(target)
            graph[target].append(value)

for i in range(1, N + 1) :
    heappush(heap, (-1 * len(graph[i]), i))


while len(heap) != 0 :
    num, index = heappop(heap)

    if (-1 * len(graph[index])) != num :
        heappush(heap, (-1 * len(graph[index]), index))
        continue

    if num == 0 :
        print(len(heap) + 1)
        
        tmp = [index]
        for i in heap :
            tmp.append(i[1])
        print(*sorted(tmp))
        exit(0)

    for i in graph[index] :
        graph[i].remove(index)









'''

5
2 4 1 5 3
4 5 1 3 2
# 3
# 3 4 5


'''