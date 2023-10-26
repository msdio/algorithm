R, C = list(map(int, input().split()))


strings = ['' for _ in range(C)]

tmp = []
for _ in range(R):
    tmp.append(input())

for i in range(len(tmp)-1, -1, -1):
    for j in range(C):
        strings[j] = strings[j] + tmp[i][j]

ans = 0
temp = -1
strings.sort()
# print(strings)

for i in range(C-1):
    str1 = strings[-1]
    str2 = strings[-2]
    strings.pop()

    t = 0
    for j in range(R):
        if str1[j] == str2[j]:
            t += 1
        else:
            break
    
    temp = max(temp, t)

print(R - temp -1 )


'''
4 6
mrvica
mrvica
marica
mateja
'''