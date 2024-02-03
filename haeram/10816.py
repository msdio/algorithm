from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))


dict = {}
for a in arr:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

ans = []
for target in targets:
    if target in dict:
        ans.append(dict[target])
    else:
        ans.append(0)

print(*ans)
