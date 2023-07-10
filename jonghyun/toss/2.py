from collections import deque


def solution(relationships, target, limit):
    graph = [[] for _ in range(110)]
    for a, b in relationships :
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)

    check = [[0] for _ in range(110)]
    dq = deque()
    dq.append((target, 0))
    check[target] = 1
    ans = 0
    while len(dq) != 0 :
        node, depth = dq.popleft()
        for i in graph[node] :
            if check[i] == 1 :
                continue
            if depth + 1 > limit :
                continue
            if depth + 1 == 1 :
                ans += 5
            else :
                ans += 11
            check[i] = 1
            dq.append((i, depth + 1))

    # print(ans)

    return ans



solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 2, 3)
