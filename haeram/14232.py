from sys import stdin

k = int(stdin.readline())

ans = []

temp = k
# 소인수 구하기
for i in range(2, k+1):
    if i*i > k or temp == 1:
        break

    while temp % i == 0:
        ans.append(i)
        temp = temp // i

if (temp != 1):
    ans.append(temp)

print(len(ans))
print(*ans)
