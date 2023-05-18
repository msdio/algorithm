# 플로이드워셜
# 그래프가 나오면 최대 노드 수 파악하기
import sys
input = sys.stdin.readline

ARRAY = ' => '
N = int(input())

dist = [[0]*52 for _ in range(52)]

alphabat = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

for _ in range(N):
    X = input().rstrip()
    s,e = X.split(ARRAY)
    if s == e:
        continue
    find_s = alphabat.find(s)
    find_e = alphabat.find(e)
    dist[find_s][find_e] = 1


resarr = []

for k in range(len(alphabat)):
    for x in range(len(alphabat)):
        for y in range(len(alphabat)):
            if dist[x][k] == 1 and dist[k][y] == 1 and x != y:
                dist[x][y] = 1


for i in range(52):
    for j in range(52):
        if dist[i][j] == 1:
            resarr.append((alphabat[i],alphabat[j]))
            


sorted_resarr = sorted(resarr, key = lambda x : (x[0],x[1]))

print(len(resarr))
for x in sorted_resarr:
    print(ARRAY.join(x))


