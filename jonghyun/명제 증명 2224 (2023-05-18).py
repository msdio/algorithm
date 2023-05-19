INF = 0xFFFFFF

graph = [[INF for j in range(130)] for _ in range(130)]

def solution():
    global graph

    N = int(input())
    for i in range(N):
        li_tmp= list(input().split(" => "))
        c1 = ord(li_tmp[0])
        c2 = ord(li_tmp[1])
        graph[c1][c2] = 0

    for k in range(130) :
        for i in range(130) :
            for j in range(130) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = 0
    for i, edge in enumerate(graph) :
        for j, node in enumerate(edge) :
            if i != j and node == 0 :
                answer += 1
    print(answer)
    for i, edge in enumerate(graph) :
        for j, node in enumerate(edge) :
            if i != j and node == 0 :
                print(chr(i), "=>", chr(j))
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

7
A => C
A => B
A => K
C => B
B => K
M => M
N => U

'''
