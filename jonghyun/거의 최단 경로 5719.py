from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')

def solution():
    N, M = list(map(int, input().split()))

    if N == 0 and M == 0:
        exit(0)
    S, D = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    reverse_graph = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = list(map(int, input().split()))
        graph[U].append((V,P))
        reverse_graph[V].append((U,P))



    def dijkstra(graph, N):
        distance = [INF for _ in range(N)]
        heap = []
        distance[S] = 0
        heappush(heap, (0, S))

        while len(heap) != 0:

            value, node_num = heappop(heap)

            if distance[node_num] != value:
                continue
            for n, d in graph[node_num]:
                
                if distance[n] > value+d:
                    distance[n] = value+d
                    heappush(heap, (value+d, n))
        return distance

    distance = dijkstra(graph, N)


    dq = deque()
    dq.append((D, distance[D]))
    remove_list = []
    while len(dq) != 0:
        node, value = dq.popleft()
        
        for i, v in enumerate(reverse_graph[node]):
            n, d = v
            if value - d == distance[n]:
                if (node, d) in graph[n]:
                    graph[n].remove((node, d))
                    dq.append((n, distance[n]))


    distance = dijkstra(graph, N)

    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])

while True:
    solution()