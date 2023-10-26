from collections import deque

N, M = list(map(int, input().split()))

ladders = {}

for _ in range(N+M):
    x, y = list(map(int, input().split()))
    ladders[x] = y

INF = 0x8FFFFFFF
check = [0 for _ in range(101)]
dq = deque()
dq.append((1,0))

while dq:
    pop, depth = dq.popleft()

    for dx in [1,2,3,4,5,6]:
        x = pop + dx
        
        if x in ladders:
            x = ladders[x]
        
        if check[x] == 1:
            continue

        if x == 100:
            print(depth+1)
            exit(0)

        check[x] = 1
        dq.append((x, depth+1))