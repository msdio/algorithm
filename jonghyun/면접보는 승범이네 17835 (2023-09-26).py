from heapq import heappush, heappop

N, M, K = list(map(int, input().split()))

distance = [0xFFFFFFFFF for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    U, V, C = list(map(int, input().split()))
    graph[V].append((U, C))

k_list= list(map(int, input().split()))

heap = []

for k in k_list:
    distance[k] = 0
    heappush(heap, (0, k))

while len(heap) != 0:
    cost, node = heappop(heap)
    
    if distance[node] != cost:
        continue
    
    for next_node, next_cost in graph[node]:
        if distance[next_node] > cost + next_cost:
            distance[next_node] = cost + next_cost
            heappush(heap, (cost + next_cost, next_node))

dis = distance[1:]
print(dis.index(max(dis)) + 1)
print(max(dis))

'''
10 9 1
10 1 5
9 1 5
5 1 5
8 1 5
7 1 5
6 1 5
4 1 5
3 1 2
2 1 5
1
'''