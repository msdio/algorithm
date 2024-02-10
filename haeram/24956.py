from sys import stdin

"""
생각을 해보자
W가 나오면 +1
H가 나오면 +1

이런식으로 세고 마지막에 계산하면 안된다.
앞에서 나온 값에 따라 의존성이 있기 때문에 
기존에 있는 개수도 확인해야 한다.

w는 그냥 w += 1
h는 앞에서 나온 w들과 짝지을 수 있으니 그 때의 w개수만큼 +, h += w
e는 좀 복잡할 것 같다.
1. 만약 e = 0이면 그냥 e += 1
2. 기존 e들과 짝지을 수 있으니 e += e

아니다 아니다
이렇게 하면 예외케이스가 너무 많이 생길 것 같다

결국 h 중심으로 왼쪽에 w가 몇갠지, 오른쪽에 e가 몇갠지 세면 될 것 같다.

h를 만날 때마다 h의 오른쪽의 e 개수를 k개라고 하면
(왼쪽의 w 개수) * (kC2 + kC3 + ... + kCk) 가 될 것 같다.
여기서 kC0 + kC1 + kC2 + ... + kCk = 2^k니까
(왼쪽의 w 개수) * (2^k - k - 1)로 바뀔 수 있을 것 같다.

그럼 w는 왼쪽에서부터, e는 오른쪽에서부터 개수 누적합을 구하면 된다.
"""
# DIVIDER = 1000000007

# n = int(stdin.readline())
# s = stdin.readline().rstrip()

# w = [0]*n
# e = [0]*n

# cnt_w = 0
# cnt_e = 0

# for i in range(n):
#     if s[i] == 'W':
#         cnt_w += 1

#     if s[n-1-i] == 'E':
#         cnt_e += 1

#     w[i] = cnt_w
#     e[n-1-i] = cnt_e

# # 이제 H 기준으로 계산만 하면 된다.
# ans = 0
# for i in range(n):
#     if s[i] == 'H':
#         # 만약 e가 1개보다 덜 남았다면 끝났다.
#         if e[i] <= 1:
#             break

#         ans += (w[i] * (2**e[i] - e[i] - 1)) % DIVIDER

# print(ans % DIVIDER)

###########################################################3

"""
가운데 h를 기준으로 왼쪽에 w가 몇개있는지, e가 몇개있는지 확인하면 된다.
w는 왼쪽 기준으로 세고, e는 오른쪽 기준으로 세야 한다.

e 개수는 2개 이상이면 되니까 kC2 + kC3 + ... + kCk = 2^k - k - 1 이다.
"""
DIVIER = 1_000_000_007

n = int(stdin.readline())
arr = stdin.readline().rstrip()

w = [0] * n
e = [0] * n

# count W and E
if arr[0] == "W":
    w[0] = 1
if arr[-1] == "E":
    e[-1] = 1

for i in range(1, n):
    if arr[i] == "W":
        w[i] = w[i - 1] + 1
    else:
        w[i] = w[i - 1]

for i in range(n - 2, -1, -1):
    if arr[i] == "E":
        e[i] = e[i + 1] + 1
    else:
        e[i] = e[i + 1]


# get answer
ans = 0
for i in range(n):
    if arr[i] != "H":
        continue

    ans += (w[i] * (2 ** e[i] - e[i] - 1)) % DIVIER

print(ans % DIVIER)
