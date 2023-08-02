from collections import deque

N, M, X = map(int, input().split())


graph = [{
  'high' : [],
  'low' : []
} for _ in range(N+ 1)]
for i in range(M) :
  a, b = map(int, input().split())
  graph[a]['low'].append(b)
  graph[b]['high'].append(a)

# print(graph)

dq = deque()
dq.append(X)

check = [0] * (N+1)

low = 0 
while len(dq) != 0 :
  pop = dq.popleft()
  
  for i in graph[pop]['low'] :

    if check[i] == 1:
      continue
    dq.append(i)
    check[i] = 1
    low += 1

dq = deque()
dq.append(X)

high = 0 
while len(dq) != 0 :
  pop = dq.popleft()
  
  for i in graph[pop]['high'] :

    if check[i] == 1:
      continue
    dq.append(i)
    check[i] = 1
    high += 1

# print(f"low, high : {low, high}")

print(f"{high + 1} {N - low}")



'''
10 5 6
1 2
2 3
3 4
4 5
3 6
# 4 10
'''