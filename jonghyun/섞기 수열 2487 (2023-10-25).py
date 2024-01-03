import math
from collections import deque


def lcm(a, b):
    return a * b // math.gcd(a, b)

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
check = [0 for _ in range(N+1)]
dq = deque()

tmp = []

for i in range(1, N+1):
    if check[i] == 1: continue
    check[arr[i]] = 1
    dq.append((arr[i], 1))
    while dq:
        pop, depth = dq.pop()
        
        if pop == i:
            tmp.append(depth)
            break
        # print(f"arr[pop] :{arr[pop]}")
        check[arr[pop]] = 1
        dq.append((arr[pop], depth + 1))

# print(tmp)
ans = tmp[0]
for i in tmp:
    ans = lcm(ans, i)

print(ans)