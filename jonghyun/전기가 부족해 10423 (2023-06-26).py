def find(x) :
    global parent
    
    if parent[x] == x :
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    global parent, check
    x = find(x) 
    y = find(y)
    if check[x] == 1 and check[y] == 1 :
        return 0

    if check[x] == 1 :
        parent[y] = x
        check[y] = 1
    elif check[y] == 1 :
        parent[x] = y   
        check[x] = 1
    else :
        parent[x] = y
    return 1



from heapq import heappush, heappop
N, M, K = list(map(int, input().split()))
check = [0] * (N + 1)
check[0] = 1
node = [[] for _ in range(N+1)]

for i in list(map(int, input().split())) :
    check[i] = 1


pq = []
for _ in range(M) :
    u, v, w = list(map(int, input().split()))
    node[u].append((v,w))
    node[v].append((u,w))
    heappush(pq , (w, u, v))

parent = [i for i in range(N+1)]
answer = 0
while len(pq) > 0 :
    w, u, v = heappop(pq)
    if find(u) == find(v) :
        continue
    
    if union(u, v) :
        answer += w
print(answer)