

graph = [[] for _ in range(100)]

def solution():
    global graph

    N = int(input())
    for i in range(N):
        li_tmp= list(input().split(" => "))
        print(li_tmp)
        c1 = ord(li_tmp[0]) - 65
        c2 = ord(li_tmp[1]) - 65

        graph[c1].append([c2, False])

    for index, edge in enumerate(graph) :
        if len(edge) != 0 :
            dfs(index)

    print(graph)


def dfs(start_point):
    global graph

    for index, edge in enumerate(graph[start_point]):
        if edge[0] == start_point :
            continue
        if edge[1] == True :
            for i in graph[edge[1]] :
                if edge not in graph[start_point]:
                    graph[start_point].append(i)
            continue
        edge[1] = True
        if edge not in graph[start_point] :
            graph[start_point].append(edge)
        dfs(start_point)


solution()

'''
2
A => b
b => C

4
A => b
b => C
C => A
A => C


5
A => B
B => C
C => D
D => A
C => A
'''
