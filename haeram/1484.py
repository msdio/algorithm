from sys import stdin

"""
a^2 - b^2 = G
(a+b)(a-b) = G

G가 10만까지니까
50000^2 - 49999^2 가 최대일듯?

그러면 1~50000 까지 돌면서 해당하는 경우 찾으면 됨
이 경우 완탐하면 25 * 10^8이니까 될 리가 없고

start, end 둘 다 0으로 시작한다음
end^2 - start^2 가 G보다 작으면 end 뒤로 보내고
G보다 크면 start를 뒤로 보내면 될듯
O(2N)으로 될 것 같다.
"""

g = int(stdin.readline())

start, end = 1, 1
ans = []

while end < 50001:
    if end * end - start * start == g:
        ans.append(end)
        end += 1
        start += 1
        continue

    if end * end - start * start < g:
        end += 1
        continue

    if end * end - start * start > g:
        start += 1
        continue

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for a in ans:
        print(a)
