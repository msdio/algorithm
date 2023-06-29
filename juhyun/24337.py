import sys
input = sys.stdin.readline


N,a,b = map(int,input().split())
big = a
mini = b - 1

flag = False # true면 마지막에 뒤집기
res = []

if b > a:
    flag = True
    big = b
    mini = a - 1

height = 0

for i in range(N):
    if big > 0:
        big -=1
        height += 1
        res.append(height)
    if big == 0 and  mini >0:
        res.append(mini)
        mini -=1


real_res = []


    


if big >0 or mini > 0 or len(res) > N:
    print(-1)
    exit()
if flag == True:
    real_res = res[::-1]
else:
    real_res = res

plus_arr = [1] * (N-len(res))

real_real_res = []



for x in real_res:
    if x >=1:
        real_real_res.append(x)
        real_real_res += plus_arr
        plus_arr = []
    else:
        real_real_res.append(x)
print(*real_real_res)