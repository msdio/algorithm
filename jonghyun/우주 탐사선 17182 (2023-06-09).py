from itertools import combinations, permutations

N, K = list(map(int, input().split()))

graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

li = [i for i in range(N)]
li.remove(K)

answer = INF = 0xFFFFFF
for p in permutations(li, len(li)) :
    cost = 0
    for index, move in enumerate(p) :
        if index == 0 :
            cost += graph[K][p[index]]
            continue
        cost += graph[p[index-1]][p[index]]
    answer = min(answer, cost)
print(answer)