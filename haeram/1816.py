from sys import stdin

n = int(stdin.readline())
num = [int(stdin.readline()) for _ in range(n)]

ans = []
for s in num:
    flag = True

    for i in range(2, 10**3):
        if (s % i == 0):
            flag = False
            break

    if (flag):
        ans.append('YES')
    else:
        ans.append('NO')

for a in ans:
    print(a)
